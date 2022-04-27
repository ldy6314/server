from blueprints.blueprint1 import bp1
from blueprints.blueprint2 import bp2
from flask import Flask


def create_app():
    app = Flask('server')
    app.register_blueprint(bp1, url_prefix='/bp1')
    app.register_blueprint(bp2, url_prefix='/bp2')
    return app


app = create_app()
app.run()
