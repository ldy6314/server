from flask import Blueprint


bp = Blueprint('bp', __name__)


@bp.route('/')
def hello_bp2():
    return "I am bp"