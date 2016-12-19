from app.database import db
from app.auth.forms import RegisterForm, LoginForm
from app.auth.models import User
from app.auth.decorators import requires_login, already_login
from werkzeug import check_password_hash, generate_password_hash
from flask import Blueprint, request, render_template, flash, g, session, \
    redirect, url_for

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/me/')
@requires_login
def home():
    return render_template("auth/profile.html", user=g.user)


@auth.before_request
def before_request():
    """pull user's profile from the database before every request are treated."""
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


@auth.route('/login/', methods=['GET', 'POST'])
@already_login
def login():
    """Login form."""
    form = LoginForm(request.form)
    # make sure data are valid, but doesn't validate password is right
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # we use werzeug to validate user's password
        if user and check_password_hash(user.password, form.password.data):
            # the session can't be modified as it's signed,
            # it's a safe place to store the user id
            session['user_id'] = user.id
            flash('Welcome back %s!' % user.name, 'alert-success')
            return redirect(url_for('restaurants.index'))
        flash('Wrong email or password', 'alert-danger')
    return render_template("auth/login.html", form=form)


@auth.route('/signup/', methods=['GET', 'POST'])
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
        session['user_id'] = user.id
        # flash will display a message to the user
        flash('Thanks you for registering %s!' % user.name, 'alert-success')
        # redirect user to the 'home' method of the user module.
        return redirect(url_for('restaurants.index'))
    return render_template("auth/signup.html", form=form)
