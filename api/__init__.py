# Flask Ext imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_htmlmin import HTMLMIN

# Common Imports
from importlib import import_module
from os import environ


__version__ = '0.1.0'

db = SQLAlchemy()
limiter = Limiter(key_func=get_remote_address)
html_minify = HTMLMIN()
migrate = Migrate()

def _check_cfg_args(config):
    assert config['SECRET_KEY'] is not None, "APP SECRET_KEY is not defined"


def initialize_extensions(app):
    db.init_app(app)
    limiter.init_app(app)
    html_minify.init_app(app)
    migrate.init_app(app, db)

def register_blueprints(app):
    for module_name in ("anthill", "site", "redirects"):
        module = import_module(f"api.{module_name}.routes")
        app.register_blueprint(module.blueprint)


def create_app(app_configuration):
    app = Flask(__name__)
    app.config.from_object(app_configuration)

    environ["APP_SETTINGS"] = str(app_configuration)
    print(f'[ENVIROMENT] {environ["APP_SETTINGS"]}')

    _check_cfg_args(app.config)

    initialize_extensions(app)
    register_blueprints(app)
    return app
