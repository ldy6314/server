from flask import Blueprint


bp1 = Blueprint('bp1', __name__)


@bp1.route('/')
def hello_bp1():
    return "I am bp1"

