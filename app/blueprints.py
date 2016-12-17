# List all Blueprint for the app here

# Api's
from api.users import users as api_handler_users
from api.welcome import welcome as api_handler_welcome

# Front end
from users.handlers import authentication as handler_authentication
from error_pages.handlers import error_pages as handler_errors
from restaurants.handlers import restaurants as handler_restaurants

