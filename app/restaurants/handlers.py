# -*- coding: utf-8 -*-
"""Resturants handlers."""

from sqlalchemy import desc
from app.database import db
from app.auth.models import User
from app.restaurants.models import Restaurant, MenuItem, menu_cources
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
    """Show all restaurants."""
    restaurants = db.session.query(
        Restaurant).order_by(desc(Restaurant.id)).all()
    return render_template('restaurants.html', restaurants=restaurants)


@restaurants.route('/restaurants/<int:id>/')
@restaurants.route('/restaurants/<int:id>/menu')
def menu(id):
    """Show restaurant menu."""
    menu = []
    restaurant = db.session.query(Restaurant).get(id)
    items = db.session.query(MenuItem).filter_by(
        restaurant_id=restaurant.id).all()
    for cource in menu_cources:
        menu.append({'id': cource['id'], 'name': cource['name'],
                     'items': [item for item in items if item.course == cource['id']]})
    return render_template('restaurants/menu.html', menu=menu, restaurant=restaurant)


@restaurants.route('/restaurants/create', methods=['GET', 'POST'])
@requires_login
def create():
    """Create restaurant."""
    if request.method == 'POST':
        restaurant = Restaurant()
        restaurant.name = request.form['name']
        restaurant.image = request.form['image']
        restaurant.description = request.form['description']
        db.session.add(restaurant)
        db.session.commit()
        flash('Restaurant <b>%s</b> was created!' %
              restaurant.name, 'alert-success')
        return redirect(url_for('restaurants.index'))
    else:
        return render_template('restaurants/form.html', restaurant=None)


@restaurants.route('/restaurants/<int:id>/edit', methods=['GET', 'POST'])
@requires_login
def edit(id):
    """Edit restaurant."""
    restaurant = db.session.query(Restaurant).get(id)
    old_name = restaurant.name
    if request.method == 'POST':
        restaurant.name = request.form['name']
        restaurant.image = request.form['image']
        restaurant.description = request.form['description']
        db.session.commit()
        flash('Restaurant <b>%s</b> was updated!' % old_name, 'alert-success')
        return redirect(url_for('restaurants.index'))
    else:
        return render_template('restaurants/form.html', restaurant=restaurant)


@restaurants.route('/restaurants/<int:id>/delete', methods=['POST'])
@requires_login
def delete(id):
    """Delete restaurant."""
    restaurant = db.session.query(Restaurant).get(id)
    flash('Restaurant <b>%s</b> was deleted!' %
          restaurant.name, 'alert-warning')
    db.session.delete(restaurant)
    db.session.commit()
    return redirect(url_for('restaurants.index'))


@restaurants.route('/restaurants/<int:id>/menu/item/create', methods=['POST'])
@requires_login
def create_menu_item(id):
    """Create menu item."""
    item = MenuItem()
    item.name = request.form['name']
    item.price = request.form['price']
    item.course = request.form['course_id']
    item.description = request.form['description']
    item.restaurant_id = request.form['restaurant_id']
    db.session.add(item)
    db.session.commit()
    flash('Menu item <b>%s</b> was created!' % item.name, 'alert-success')
    return redirect(url_for('restaurants.menu', id=item.restaurant_id))


@restaurants.route('/restaurants/menu/item/<int:id>/edit', methods=['POST'])
@requires_login
def edit_menu_item(id):
    """Edit menu item."""
    item = db.session.query(MenuItem).get(id)
    old_name = item.name
    item.name = request.form['name']
    item.price = request.form['price']
    item.course = request.form['course_id']
    item.description = request.form['description']
    db.session.commit()
    flash('Menu item <b>%s</b> was updated!' % old_name, 'alert-success')
    return redirect(url_for('restaurants.menu', id=item.restaurant.id))


@restaurants.route('/restaurants/menu/item/<int:id>/delete', methods=['POST'])
@requires_login
def delete_menu_item(id):
    """Delete menu item."""
    item = db.session.query(MenuItem).get(id)
    restaurant = item.restaurant
    message = 'Menu item <b>%s</b> was deleted from restaurant <b>%s</b>!'
    flash(message % (item.name, restaurant.name), 'alert-warning')
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('restaurants.menu', id=restaurant.id))
