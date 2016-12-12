from flask import Flask
application = Flask(__name__)

# TODO:
# See how can we use Blueprints to avoid Circular Imports.
# http://flask.pocoo.org/docs/0.11/blueprints/#blueprints
import app.router