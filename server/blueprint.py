from flask import Blueprint, jsonify, request
from .models import People
from .extentions import db

bp = Blueprint('bp', __name__)


@bp.before_app_first_request
def init_database():
    db.create_all()


@bp.route('/')
def hello():
    return jsonify(
        {
            'name': 'ldy6314',
            'age': 35
        }
    )


@bp.route('/get_all')
def get_all():
    res = People.query.all()
    print(res)
    res = list(map(lambda x: {'id': x.id, 'name': x.name, 'age': x.age}, res))
    print(res)
    return jsonify(
        res
    )


@bp.route('/set_all')
def set_all():
    infos = [
        {
            'name': '张三',
            'age': 18
        },
        {
            'name': '李四',
            'age': 19
        },
        {
            'name': '王二麻',
            'age': 20
        },
        {
            'name': '尼古拉斯',
            'age': 66
        }
    ]
    for info in infos:
        person = People(name=info['name'], age=info['age'])
        db.session.add(person)
    db.session.commit()
    return jsonify("add success")


@bp.route('/clear_all')
def clear_all():
    persons = People.query.all()
    for person in persons:
        db.session.delete(person)
    db.session.commit()
    return 'clear'


@bp.route('/add_student', methods=['POST'])
def add_student():
    data = request.get_json()
    name, age = data['name'], data['age']
    response = dict()
    res = People.query.filter(People.name == name).first()
    if not res:
        person = People(name=name, age=age)
        db.session.add(person)
        db.session.commit()
    response['result'] = 'fail' if res else 'success'

    return jsonify(response)

