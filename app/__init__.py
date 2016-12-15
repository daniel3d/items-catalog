import config
import models
import inspect
import blueprints

from flask import Flask, Blueprint

__all__ = ['init_app', 'config', 'blueprints']


def init_app(default_config=None, default_name=None, default_blueprints=None):
    """Create a Flask app."""

    if default_config is None:
        default_config = config
    if default_name is None:
        default_name = config.PROJECT
    if default_blueprints is None:
        default_blueprints = blueprints

    app = Flask(default_name)
    configure_app(app, default_config)
    configure_blueprints(app, default_blueprints)
    configure_error_handlers(app)
    return app


def configure_app(app, config):
    """Different ways of configurations."""
    app.version = config.VERSION
    app.config.from_object(config)


def configure_blueprints(app, blueprints):
    """Register the blueprints."""
    if inspect.ismodule(blueprints):
        for name, blueprint in inspect.getmembers(blueprints):
            if isinstance(blueprint, Blueprint):
                print(" * Register Blueprint: [ %s ]" % name)
                app.register_blueprint(blueprint)
    else:
        for blueprint in blueprints:
            if isinstance(blueprint, Blueprint):
                app.register_blueprint(blueprint)


def configure_error_handlers(app):
    """Configure the error pages."""
    @app.errorhandler(500)
    def server_error_page(error):
        return "ERROR PAGE!"