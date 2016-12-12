"""
 Simple API endpoint for returning welcome message
"""
from flask import Blueprint, render_template, current_app, request, flash, \
    url_for, redirect, session, abort, jsonify, \
    make_response

welcome = Blueprint('welcome', __name__, url_prefix='/api/welcome')


@welcome.route('/', methods=['GET'])
def index():
    data = {
        'message': "welcome to " + current_app.name,
        'version': current_app.version
    }
    return make_response(jsonify(data))
