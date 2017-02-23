# -*- coding: utf-8 -*-
"""Auth models."""

from app.database import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """Registered user capable of viewing and editing.

    :param str name: name of the user
    :param str email: email address of user
    :param str password: encrypted password for the user

    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String, nullable=True)
    username = db.Column(db.String(64), nullable=True)
    social_id = db.Column(db.String(64), nullable=True, unique=True)
