from flask import Flask
from .settings import Settings
from .extentions import db
from .blueprint import bp
from flask_cors import CORS


def create_app():
    app = Flask('server')
    app.config.from_object(Settings)
    db.init_app(app)
    CORS(app, supports_credentials=True)
    app.register_blueprint(bp)
    return app
