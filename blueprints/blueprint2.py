from flask import Blueprint


bp2 = Blueprint('bp2', __name__)


@bp2.route('/')
def hello_bp2():
    return "I am bp2"
