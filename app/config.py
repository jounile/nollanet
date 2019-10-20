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

    # File upload
    UPLOAD_FOLDER = '/Users/jouni.leino/Git/jounile/nollanet/app/static/media'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

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

    AZURE_ACCOUNT = os.getenv('AZURE_ACCOUNT')
    AZURE_KEY = os.getenv('AZURE_STORAGE_KEY')
    AZURE_CONTAINER = os.getenv('AZURE_CONTAINER')

    # Facebook
    USER_SHORT_TOKEN = os.getenv('USER_SHORT_TOKEN')
    USER_LONG_TOKEN = 'None'
    APP_ID = os.getenv('APP_ID')
    APP_SECRET = os.getenv('APP_SECRET')
    PAGE_TOKEN = 'None'
    FACEBOOK_PAGE_ID = os.getenv('FACEBOOK_PAGE_ID')