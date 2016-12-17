from app import db
from flask import Blueprint, render_template, current_app, request, flash, \
    url_for, redirect, session

authentication = Blueprint('authentication', __name__, url_prefix='/auth')


@authentication.route('/login')
def login():
	# admin = User('admin', 'admin@example.com')
	# guest = User('guest', 'guest@example.com')
	# db.session.add(admin)
	# db.session.add(guest)
	# db.session.commit()
	return render_template('auth.login.html')

@authentication.route('/signup')
def signup():
	return render_template('auth.signup.html')
