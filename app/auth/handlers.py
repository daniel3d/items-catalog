# -*- coding: utf-8 -*-
"""Auth handlers."""

from app.oauth import OAuthSignIn
from app.database import db
from app.login_manager import login_manager
from app.auth.forms import RegisterForm, LoginForm
from app.auth.models import User
from app.auth.decorators import requires_login, already_login
from werkzeug import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, current_user
from flask import Blueprint, request, render_template, flash, g, session, \
    redirect, url_for

auth = Blueprint('auth', __name__, url_prefix='/auth')

login_manager.view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    """Load user by id."""
    return User.query.get(int(user_id))


@auth.route('/me/')
@requires_login
def home():
    """User homepage TODO."""
    return render_template("auth/profile.html", user=g.user)


@auth.before_request
def before_request():
    """pull user's profile from the database before every request are treated."""
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


@auth.route('/login', methods=['GET', 'POST'])
@already_login
def login():
    """Login form."""
    form = LoginForm(request.form)
    # make sure data are valid, but doesn't validate password is right
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # first check if user already registered with oauth
        if user.social_id:
            provider, token = user.social_id.split('$')
            flash('You have already accout via %s' % provider, 'alert-warning')
            return redirect(url_for('auth.login'))
        # check if password is corect
        if user and check_password_hash(user.password, form.password.data):
            # the session can't be modified as it's signed,
            # it's a safe place to store the user id
            login_user(user, True)
            flash('Welcome back %s!' % user.name, 'alert-success')
            return redirect(url_for('restaurants.index'))
        flash('Wrong email or password', 'alert-danger')
    return render_template("auth/login.html", form=form)


@auth.route('/signup', methods=['GET', 'POST'])
@already_login
def signup():
    """Registration Form."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        # create an user instance not yet stored in the database
        user = User(name=form.name.data, email=form.email.data,
                    password=generate_password_hash(form.password.data))
        # Insert the record in our database and commit it
        db.session.add(user)
        db.session.commit()
        # Log the user in, as he now has an id

        load_user(user.id)
        #session['user_id'] = user.id

        # flash will display a message to the user
        flash('Thanks you for registering %s!' % user.name, 'alert-success')
        # redirect user to the 'home' method of the user module.
        return redirect(url_for('restaurants.index'))
    return render_template("auth/signup.html", form=form)


@auth.route('/logout')
def logout():
    """Log out the user."""
    logout_user()
    return redirect(url_for('restaurants.index'))


@auth.route('/<provider>')
def oauth_authorize(provider):
    """Authorize with by given provide."""
    if not current_user.is_anonymous:
        return redirect(url_for('restaurants.index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@auth.route('/callback/<provider>')
def oauth_callback(provider):
    """Callback for the oauth provides."""
    if not current_user.is_anonymous:
        return redirect(url_for('restaurants.index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.', 'alert-danger')
        return redirect(url_for('restaurants.index'))

    user = User.query.filter_by(email=email).first()
    if user and not user.social_id:
        user.social_id = social_id
        user.username = username
        db.session.add(user)
        db.session.commit()
    else:
        user = User.query.filter_by(social_id=social_id).first()
        if not user:
            user = User(social_id=social_id, username=username, email=email)
            db.session.add(user)
            db.session.commit()

    login_user(user, True)
    flash('Welcome %s!' % username, 'alert-success')
    return redirect(url_for('restaurants.index'))
