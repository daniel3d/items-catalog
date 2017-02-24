# -*- coding: utf-8 -*-
"""Default config file."""

# Project details
CREATOR = "Daniel Yovchev"
PROJECT = "Items Catalog"
VERSION = "0.0.2"

# Server details
PORT = 5000
DEBUG = True
HOST = "0.0.0.0"

# Secret key
SECRET_KEY = "base64:VWRhY2l0eSBGdWxsIFN0YWNrIFdlYiBEZXZlbG9wZXIgTmFub2RlZ3JlZQ=="

# Database
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Oauth credentials
OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '355967214785654',
        'secret': 'b82dd562d20668c95dc822ce6a1b55d6'
    },
	'google': {
		'id': '779916243668-f149orlcgna9crvhmji4m6sa4a5086eo.apps.googleusercontent.com',
		'secret': 'vMARc1lYx21dei8GEwoQLRxr'
	},
    'twitter': {
        'id': '	EAhO6zLLTFaPsxElQEQxrHvaT',
        'secret': 'lUooJ0mMEPL3oo9k8cndvt9WR57tDimGxp8WQkC7ryO6BVvXRd'
    }
}
