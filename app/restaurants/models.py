# -*- coding: utf-8 -*-
"""Resturants models."""

from app.database import db
from app.auth.models import User

menu_cources = [
    {'id': 1, 'name': 'Starters'},
    {'id': 2, 'name': 'House specials'},
    {'id': 3, 'name': 'Meal deals'},
    {'id': 4, 'name': 'Drinks and desserts'},
]
"""Harcoded menu courses that we use to divide the menu items in categories."""

class Restaurant(db.Model):
    """The model for resturants."""

    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    image = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.String(64), nullable=False)
    user = db.relationship(User)

    def as_dict(self):
        """Convert model to dict."""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class MenuItem(db.Model):
    """The model for menu items."""

    __tablename__ = 'menu_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    price = db.Column(db.String(8))
    course = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship(User)
    description = db.Column(db.String(64), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    restaurant = db.relationship(Restaurant)

    def as_dict(self):
        """Convert model to dict."""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
