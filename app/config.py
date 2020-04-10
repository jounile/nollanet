# config.py

import os

class DefaultConfig(object):

    DEBUG = True
    TESTING = False

    TITLE = 'nolla.net'

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    APP_STATIC = os.path.join(APP_ROOT, 'static')

    SESSION_TYPE = 'filesystem'
    SECRET_KEY = os.getenv('SECRET_KEY') or os.urandom(24)

    # Pagination
    PER_PAGE = 10
    CSS_FRAMEWORK = 'bootstrap4'
    LINK_SIZE = 'sm'
    SHOW_SINGLE_PAGE = False  # decide whether or not a single page returns pagination

    # Bcrypt algorithm hashing rounds
    BCRYPT_LOG_ROUNDS = 5

    # File upload
    UPLOAD_FOLDER = '/Users/jouni.leino/Git/jounile/nollanet/app/static/media'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # DB connection params
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB = os.getenv('MYSQL_DB')

    # SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://' + MYSQL_USER + ':' + MYSQL_PASSWORD + '@' + MYSQL_HOST + '/' + MYSQL_DB
    #SQLALCHEMY_POOL_PRE_PING = True
    #SQLALCHEMY_POOL_RECYCLE = 3600
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 3600,
        'pool_pre_ping': True,
        'connect_args': {
            'connect_timeout': 5
        }
    }

    # ReCaptcha
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')
    RECAPTCHA_OPTIONS = {'theme':'black'}

    # Youtube
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

    # Azure Blob Storage
    AZURE_BLOB_URI = os.getenv('AZURE_BLOB_URI')
    AZURE_ACCOUNT = os.getenv('AZURE_ACCOUNT')
    AZURE_STORAGE_KEY = os.getenv('AZURE_STORAGE_KEY')
    AZURE_CONTAINER = os.getenv('AZURE_CONTAINER')

    # Facebook
    USER_SHORT_TOKEN = os.getenv('USER_SHORT_TOKEN')
    USER_LONG_TOKEN = 'None'
    APP_ID = os.getenv('APP_ID')
    APP_SECRET = os.getenv('APP_SECRET')
    PAGE_TOKEN = 'None'
    FACEBOOK_PAGE_ID = os.getenv('FACEBOOK_PAGE_ID')

    # SendGrid
    SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
    NOLLANET_EMAIL = os.getenv("NOLLANET_EMAIL")

    APPINSIGHTS_INSTRUMENTATIONKEY = os.getenv("APPINSIGHTS_INSTRUMENTATIONKEY")