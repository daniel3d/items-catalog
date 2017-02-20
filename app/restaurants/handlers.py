from sqlalchemy import desc
from app.database import db
from app.auth.models import User
from app.restaurants.models import Restaurant
from app.auth.decorators import requires_login
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
	#show full list of restaurants.
	restaurants = db.session.query(Restaurant).order_by(desc(Restaurant.id)).all()
	return render_template('restaurants.html', restaurants=restaurants)


@restaurants.route('/restaurants/<int:restaurant>/')
@restaurants.route('/restaurants/<int:restaurant>/menu')
def menu(restaurant):
	#show full list of restaurants.
	restaurant = db.session.query(Restaurant).get(restaurant)
	return render_template('restaurants/menu.html', restaurant=restaurant)


@restaurants.route('/restaurants/<int:restaurant>/edit', methods=['GET', 'POST'])
def edit(restaurant):
	#show full list of restaurants.
	restaurant = db.session.query(Restaurant).get(restaurant)
	old_name = restaurant.name
	if request.method == 'POST':
		restaurant.name = request.form['name']
		restaurant.image = request.form['image']
		restaurant.description = request.form['description']
		db.session.commit()
		flash('Restaurant %s was updated!' % old_name, 'alert-success')
		return redirect(url_for('restaurants.index'))
	else:
		return render_template('restaurants/form.html', restaurant=restaurant)


@restaurants.route('/restaurants/<int:restaurant>/delete')
def delete(restaurant):
	#show full list of restaurants.
	restaurant = db.session.query(Restaurant).get(restaurant)
	flash('Restaurant %s was deleted!' % restaurant.name, 'alert-danger')
	db.session.delete(restaurant)
	db.session.commit()
	return redirect(url_for('restaurants.index'))


@restaurants.route('/restaurants/create', methods=['GET', 'POST'])
@requires_login
def create():
	if request.method == 'POST':
		restaurant = Restaurant()
		restaurant.name = request.form['name']
		restaurant.image = request.form['image']
		restaurant.description = request.form['description']
		db.session.add(restaurant)
		db.session.commit()
		flash('Restaurant %s was created!' % restaurant.name, 'alert-success')
		return redirect(url_for('restaurants.index'))
	else:
		return render_template('restaurants/form.html', restaurant=None)