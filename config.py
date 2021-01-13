import os

from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'top-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_CONNECTION') or \
        'sqlite:///' + os.path.join(basedir, 'memory.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 50
