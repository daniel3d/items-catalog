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


# <Config {
#
# 'JSON_AS_ASCII': True,
# 'USE_X_SENDFILE': False,
#
# 'VERSION': '0.0.1',
#
# 'SESSION_COOKIE_PATH': None,
# 'SESSION_COOKIE_DOMAIN': None,
# 'SESSION_COOKIE_NAME': 'session',
#
# 'PROJECT': 'Items Catalog',
#
# 'SESSION_REFRESH_EACH_REQUEST': True,
# 'LOGGER_HANDLER_POLICY': 'always',
# 'LOGGER_NAME': 'Items Catalog',
# 'DEBUG': True,
# 'SECRET_KEY': 'secret key',
# 'EXPLAIN_TEMPLATE_LOADING': False,
# 'PORT': 5000,
#
# 'DESCRIPTION': 'Project for udacity full stack devolempent',
#
# 'MAX_CONTENT_LENGTH': None,
# 'APPLICATION_ROOT': None,
# 'SERVER_NAME': None,
# 'PREFERRED_URL_SCHEME': 'http',
# 'JSONIFY_PRETTYPRINT_REGULAR': True,
# 'TESTING': False,
# 'HOST': '0.0.0.0',
# 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31),
# 'PROPAGATE_EXCEPTIONS': None,
# 'TEMPLATES_AUTO_RELOAD': None,
# 'TRAP_BAD_REQUEST_ERRORS': False,
# 'JSON_SORT_KEYS': True,
# 'JSONIFY_MIMETYPE': 'application/json',
# 'SESSION_COOKIE_HTTPONLY': True,
# 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200),
# 'PRESERVE_CONTEXT_ON_EXCEPTION': None,
# 'SESSION_COOKIE_SECURE': False,
# 'TRAP_HTTP_EXCEPTIONS': False
#
# }>
