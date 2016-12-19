from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required, EqualTo, Email

class LoginForm(FlaskForm):
  email = TextField('Email address', [Required(), Email()])
  password = PasswordField('Password', [Required()])

class RegisterForm(FlaskForm):
  name = TextField('Name', [Required()])
  email = TextField('Email address', [Required(), Email()])
  password = PasswordField('Password', [Required()])
  confirm = PasswordField('Repeat Password', [
	Required(), EqualTo('password', message='Passwords must match')])