# List all Blueprint for the app here

#from api import welcome as api_welcome
from .users.handlers import authentication as handler_authentication
from .error_pages.handlers import error_pages as handler_errors
from .restaurants.handlers import restaurants as handler_restaurants

