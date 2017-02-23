# -*- coding: utf-8 -*-
"""Errors handlers."""

from flask import Blueprint, render_template, current_app, request, flash, \
    url_for, redirect, session

errors = Blueprint('errors', __name__,)


@errors.app_errorhandler(500)
def server_error_page(error):
    """Handle 500 error."""
    return render_template('errors/503.html')


@errors.app_errorhandler(404)
def server_error_page(error):
    """Handle 404 error."""
    return render_template('errors/404.html')
