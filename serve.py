# -*- coding: utf-8 -*-
"""The entry point of the application."""

from app import create_app, config

# Project information
config.CREATOR = "Daniel Yovchev"
config.PROJECT = "Items Catalog"
config.VERSION = "0.0.1"

# Server information
config.PORT = 5000
config.DEBUG = True
config.HOST = "0.0.0.0"

# Make sure we update this key in production.
config.SECRET_KEY = "base64:VWRhY2l0eSBGdWxsIFN0YWNrIFdlYiBEZXZlbG9wZXIgTmFub2RlZ3JlZQ=="

# Set the oauth credentials.
config.OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '355967214785654',
        'secret': 'b82dd562d20668c95dc822ce6a1b55d6'
    },
    'twitter': {
        'id': '',
        'secret': ''
    }
}

if __name__ == '__main__':
    # Start the app if we are running this from terminal.
    create_app(config).run(host=config.HOST,
                           port=config.PORT, debug=config.DEBUG)
