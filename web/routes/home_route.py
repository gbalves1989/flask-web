from flask import Blueprint
from flask_login import login_required
from ..services.home_service import list_home


home_blueprint = Blueprint('home_routes', __name__)


@home_blueprint.route('/')
@login_required
def page_home():
    return list_home()
