# -*- coding: utf-8 -*-
"""Help welcome api for the app."""

from flask import Blueprint, render_template, current_app, request, flash, \
    url_for, redirect, session, abort, jsonify, \
    make_response

welcome = Blueprint('api.welcome', __name__, url_prefix='/api/welcome')


@welcome.route('/', methods=['GET'])
def index():
    """Welcome app information."""
    data = {
        'creator': current_app.config['CREATOR'],
        'message': "Welcome to `%s` public api" % current_app.config['PROJECT'],
        'version': current_app.config['VERSION'],
        'resources': [
            {
                'name': 'Restorants',
                'link': 'http://localhost:5000/api/restorants'
            }
        ]
    }
    return make_response(jsonify(data))
