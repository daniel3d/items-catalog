# List all Blueprint for the app here

# Api's
from api.users import users as api_handler_users
from api.welcome import welcome as api_handler_welcome

# Front end
from auth.handlers import auth as handler_auth
from errors.handlers import errors as handler_errors
from restaurants.handlers import restaurants as handler_restaurants

