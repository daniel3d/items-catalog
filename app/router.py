from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

router = Blueprint('router', __name__, template_folder='views')

@router.route('/', defaults={'page': 'index'})
@router.route('/<page>')
def show(page):
	return 'Hello World!'
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)