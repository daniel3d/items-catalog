from flask import Blueprint, render_template, current_app, request, flash, \
    url_for, redirect, session

error_pages = Blueprint('error_pages', __name__,)


@error_pages.app_errorhandler(500)
def server_error_page(error):
    return render_template('errors/503.html')

@error_pages.app_errorhandler(404)
def server_error_page(error):
    return render_template('errors/404.html')
