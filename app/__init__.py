from flask import Flask
from app.router import router
application = Flask(__name__)

# TODO:
# Use http://blog.sampingchuang.com/flask-hello-world/ to create structure
# See how can we use Blueprints to avoid Circular Imports.
# http://flask.pocoo.org/docs/0.11/blueprints/#blueprints
app.register_blueprint(router)