from app.auth.models import User
from flask import Blueprint, g, render_template, current_app, request, flash, \
    url_for, redirect, session

restaurants = Blueprint('restaurants', __name__)

@restaurants.before_request
def before_request():
    """pull user's profile from the database before every request are treated."""
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])

@restaurants.route('/')
@restaurants.route('/restaurants')
def index():
	#return current_app.template_folder
	return render_template('restaurants.html')
