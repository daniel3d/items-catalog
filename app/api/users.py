from app.database import db
from app.auth.models import User
from flask import Blueprint, url_for, redirect, jsonify, make_response

users = Blueprint('api.users', __name__, url_prefix='/api/users')


@users.route('/', methods=['GET'])
def all():
    users = User.query.all()
    return make_response(jsonify([u.serialize for u in users]))


@users.route('/create', methods=['GET', 'POST'])
def create():
    admin = User()
    admin.username = 'admin'
    admin.email = 'admin@example.com'
    db.session.add(admin)

    guest = User()
    guest.username = 'guest'
    guest.email = 'guest@example.com'
    db.session.add(guest)
    
    db.session.commit()
    return redirect(url_for('api.users.all'))
