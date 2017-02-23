# -*- coding: utf-8 -*-
"""Item catalog application."""

import os
import sys
import inspect

from app.database import db
from app.login_manager import login_manager
from flask import Flask, Blueprint


def log(message):
    """Use logger so we don't print multiple times when reload is on."""
    if not os.environ.get('WERKZEUG_RUN_MAIN'):
        print message


def create_app(default_config=None, default_blueprints=None):
    """Create a Flask app."""
    def configure_app():
        """Set up the app."""
        app.version = default_config.VERSION
        app.config.from_object(default_config)
        login_manager.init_app(app)
        log(" * Configuring app: `%s` version: %s" % (app.name, app.version))

    def configure_database():
        """Set up the database."""
        db.init_app(app)
        with app.test_request_context():
            db.create_all()
        log(" * Init database: `%s`" % app.config['SQLALCHEMY_DATABASE_URI'])

    def configure_blueprints():
        """Load the curent blueprients."""
        if inspect.ismodule(default_blueprints):
            for name, blueprint in inspect.getmembers(default_blueprints):
                if isinstance(blueprint, Blueprint):
                    app.register_blueprint(blueprint)
                    log(" * Registrated Blueprint: `%s`" % name)
        else:
            for blueprint in default_blueprints:
                if isinstance(blueprint, Blueprint):
                    app.register_blueprint(blueprint)
            log(" * Custom Blueprints Registrated")

    # Set app defaults
    if default_config is None:
        import config
        default_config = config
    if default_blueprints is None:
        import blueprints
        default_blueprints = blueprints

    # Create the curent app
    app = Flask(default_config.PROJECT)

    # Configure the curent app
    configure_app()
    configure_database()
    configure_blueprints()

    return app
