# -*- coding: utf-8 -*-
"""List all Blueprint for the app here."""

# Api's
from api.welcome import welcome as api_handler_welcome
from api.restaurants import restaurants as api_handler_restaurants

# Front end
from auth.handlers import auth as handler_auth
from errors.handlers import errors as handler_errors
from restaurants.handlers import restaurants as handler_restaurants
