# config.py

import os

class DefaultConfig(object):

    DEBUG = True
    TESTING = False

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    APP_STATIC = os.path.join(APP_ROOT, 'static')

    SESSION_TYPE = 'filesystem'
    SECRET_KEY = os.getenv('SECRET_KEY') or os.urandom(24)

    # Pagination
    PER_PAGE = 10
    CSS_FRAMEWORK = 'bootstrap3'
    LINK_SIZE = 'sm'
    SHOW_SINGLE_PAGE = False  # decide whether or not a single page returns pagination

    # Bcrypt algorithm hashing rounds
    BCRYPT_LOG_ROUNDS = 5

    # DB connection params
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB = os.getenv('MYSQL_DB')
    MYSQL_PORT = 3306

    # ReCaptcha
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')
    RECAPTCHA_OPTIONS = {'theme':'black'}

    # Youtube
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

    # Azure Blob Storage
    AZURE_BLOB = os.getenv('AZURE_BLOB')
