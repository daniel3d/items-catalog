from flask import Blueprint, render_template, current_app, request, flash, \
    url_for, redirect, session

authentication = Blueprint('authentication', __name__, url_prefix='/auth')


@authentication.route('/login')
def login():
	return render_template('auth.login.html')

@authentication.route('/signup')
def signup():
	return render_template('auth.signup.html')
