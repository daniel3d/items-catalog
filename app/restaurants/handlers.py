# -*- coding: utf-8 -*-
"""Resturants handlers."""

from sqlalchemy import desc
from app.database import db
from app.auth.models import User
from app.restaurants.models import Restaurant, MenuItem, menu_cources
from app.auth.decorators import login_required
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
    if g.user is None:
        restaurants = db.session.query(
            Restaurant).order_by(desc(Restaurant.id)).all()
    else:
        restaurants = db.session.query(Restaurant).filter_by(
            user_id=g.user.id).order_by(desc(Restaurant.id)).all()
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
@login_required
def create():
    """Create restaurant."""
    if request.method == 'POST':
        restaurant = Restaurant()
        restaurant.name = request.form['name']
        restaurant.image = request.form['image']
        restaurant.description = request.form['description']
        restaurant.user_id = g.user.id
        db.session.add(restaurant)
        db.session.commit()
        flash('Restaurant <b>%s</b> was created!' %
              restaurant.name, 'alert-success')
        return redirect(url_for('restaurants.index'))
    else:
        return render_template('restaurants/form.html', restaurant=None)


@restaurants.route('/restaurants/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    """Edit restaurant."""
    restaurant = db.session.query(Restaurant).get(id)
    if restaurant.user.id == g.user.id:
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
    else:
        flash(u'You dont have access to edit this restaurant.', 'alert-danger')
        return redirect(url_for('restaurants.index'))

@restaurants.route('/restaurants/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    """Delete restaurant."""
    restaurant = db.session.query(Restaurant).get(id)
    if restaurant.user.id == g.user.id:
        flash('Restaurant <b>%s</b> was deleted!' %
              restaurant.name, 'alert-warning')
        db.session.delete(restaurant)
        db.session.commit()
        return redirect(url_for('restaurants.index'))
    else:
        flash(u'You dont have access to delete this restaurant.', 'alert-danger')
        return redirect(url_for('restaurants.index'))

@restaurants.route('/restaurants/<int:id>/menu/item/create', methods=['POST'])
@login_required
def create_menu_item(id):
    """Create menu item."""
    restaurant = db.session.query(Restaurant).get(id)
    if restaurant.user.id == g.user.id:
        item = MenuItem()
        item.name = request.form['name']
        item.price = request.form['price']
        item.course = request.form['course_id']
        item.description = request.form['description']
        item.restaurant_id = restaurant.id
        item.user_id = restaurant.user.id
        db.session.add(item)
        db.session.commit()
        flash('Menu item <b>%s</b> was created!' % item.name, 'alert-success')
        return redirect(url_for('restaurants.menu', id=item.restaurant_id))
    else:
        flash(u'You dont have access for adding menu items to this restaurant.', 'alert-danger')
        return redirect(url_for('restaurants.index'))

@restaurants.route('/restaurants/menu/item/<int:id>/edit', methods=['POST'])
@login_required
def edit_menu_item(id):
    """Edit menu item."""
    item = db.session.query(MenuItem).get(id)
    if item.user.id == g.user.id:
        old_name = item.name
        item.name = request.form['name']
        item.price = request.form['price']
        item.course = request.form['course_id']
        item.description = request.form['description']
        db.session.commit()
        flash('Menu item <b>%s</b> was updated!' % old_name, 'alert-success')
        return redirect(url_for('restaurants.menu', id=item.restaurant.id))
    else:
        flash(u'You dont have access to edit this menu item.', 'alert-danger')
        return redirect(url_for('restaurants.index'))

@restaurants.route('/restaurants/menu/item/<int:id>/delete', methods=['POST'])
@login_required
def delete_menu_item(id):
    """Delete menu item."""
    item = db.session.query(MenuItem).get(id)
    if item.user.id == g.user.id:
        restaurant = item.restaurant
        message = 'Menu item <b>%s</b> was deleted from restaurant <b>%s</b>!'
        flash(message % (item.name, restaurant.name), 'alert-warning')
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('restaurants.menu', id=restaurant.id))
    else:
        flash(u'You dont have access to delete this menu item.', 'alert-danger')
        return redirect(url_for('restaurants.index'))