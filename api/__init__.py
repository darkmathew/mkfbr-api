from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask

__version__ = '0.1.0'

def _check_cfg_args(config):
    assert config['SECRET_KEY'] is not None, (
        "APP SECRET_KEY is not defined"
    )


def create_app(app_configuration):
    app = Flask(__name__)
    app.config.from_object(app_config)
    _check_cfg_args(app_config)