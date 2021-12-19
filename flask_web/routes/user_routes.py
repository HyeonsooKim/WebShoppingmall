# user_routes.py

from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/')
def index():
    return 'User index page'