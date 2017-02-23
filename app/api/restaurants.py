# -*- coding: utf-8 -*-
"""Resturants api."""

from sqlalchemy import desc
from app.database import db
from app.restaurants.models import Restaurant, MenuItem, menu_cources
from flask import Blueprint, url_for, redirect, jsonify, make_response

restaurants = Blueprint('api.restaurants', __name__,
                        url_prefix='/api/restaurants')


@restaurants.route('/', methods=['GET'])
def all():
    """Get all resturants as json output."""
    restaurants = db.session.query(
        Restaurant).order_by(desc(Restaurant.id)).all()
    return make_response(jsonify([r.as_dict() for r in restaurants]))


@restaurants.route('/<int:id>/', methods=['GET'])
@restaurants.route('/<int:id>/menu', methods=['GET'])
def menu(id):
    """Get all menu items as json output."""
    menu = []
    r = db.session.query(Restaurant).get(id)
    items = db.session.query(MenuItem).filter_by(restaurant_id=r.id).all()
    for cource in menu_cources:
        menu.append({'id': cource['id'], 'name': cource['name'],
                     'items': [i.as_dict() for i in items if i.course == cource['id']]})
    return make_response(jsonify(menu))
