import os

# Project details
PROJECT = "items-catalog"
VERSION = "0.0.1"

# Paths
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_TEMPLATES = os.path.join(PROJECT_ROOT, 'templates')

# Server
PORT = 5000
DEBUG = True
HOST = '0.0.0.0'

# Secret key for signing cookies
# http://flask.pocoo.org/docs/quickstart/#sessions
SECRET_KEY = 'secret key'
