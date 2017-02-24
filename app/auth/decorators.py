# -*- coding: utf-8 -*-
"""Auth decorators."""

from functools import wraps
from flask import g, flash, redirect, url_for, request


def login_required(f):
    """Use to make sure login user is required."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            flash(u'Please login to view this page.', 'alert-danger')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


def already_login(f):
    """Check if user is already login."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user:
            return redirect(url_for('restaurants.index'))
        return f(*args, **kwargs)
    return decorated_function
