# -*- coding: utf-8 -*-
"""The entry point of the application."""

from app import create_app, config

if __name__ == '__main__':
    # Start the app if we are running this from terminal.
    create_app(config).run(host=config.HOST,
                           port=config.PORT, debug=config.DEBUG)
