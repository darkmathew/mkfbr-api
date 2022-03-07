from string import ascii_letters, digits
from random import choice
from os.path import abspath, dirname, join as path_join
from os import environ

basedir = abspath(dirname(__file__))


def generate_random_key():
    key = ''.join(
        choice(ascii_letters) + choice(str(digits)) + choice("$%ç!?,.:;")
        for i in range(20)
    )
    return key


class Config(object):
    MINIFY_HTML = True
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = None
    SECRET_KEY = None
    STATIC_FOLDER = 'static'
    

class ProductionConfiguration(Config):
    environ['APP_SETTINGS'] = "api.config.ProductionConfiguration"
    DEBUG = False
    SECRET_KEY = generate_random_key()
    DB_FILE = path_join(basedir, 'database', 'address.db')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_FILE}'


class DebugConfiguration(Config):
    environ['APP_SETTINGS'] = "api.config.DebugConfiguration"
    DEBUG = True
    SECRET_KEY = generate_random_key()
    DB_FILE = path_join(basedir, 'database', 'address.db')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_FILE}'


config_dict = {
    "Production": ProductionConfiguration,
    "Debug": DebugConfiguration,
}
