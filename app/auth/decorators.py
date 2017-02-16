from functools import wraps

from flask import g, flash, redirect, url_for, request

def requires_login(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if g.user is None:
			flash(u'Please login to view this page.', 'alert-danger')
			return redirect(url_for('auth.login'))
		return f(*args, **kwargs)
	return decorated_function

def already_login(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if g.user:
			return redirect(url_for('restaurants.index'))
		return f(*args, **kwargs)
	return decorated_function