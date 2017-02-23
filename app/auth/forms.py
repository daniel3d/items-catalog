# -*- coding: utf-8 -*-
"""Auth form validations."""

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required, EqualTo, Email


class LoginForm(FlaskForm):
	"""Login form validation."""

	email = TextField('Email address', [Required(), Email()])
	password = PasswordField('Password', [Required()])


class RegisterForm(FlaskForm):
	"""Register form validation."""

	name = TextField('Name', [Required()])
	email = TextField('Email address', [Required(), Email()])
	password = PasswordField('Password', [Required()])
	confirm = PasswordField('Repeat Password', [
        Required(), EqualTo('password', message='Passwords must match')])
