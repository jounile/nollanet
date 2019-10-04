# config.py

import os

class DefaultConfig(object):

    DEBUG = True
    TESTING = False

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    APP_STATIC = os.path.join(APP_ROOT, 'static')

    SESSION_TYPE = 'filesystem'

    # Pagination
    PER_PAGE = 10
    CSS_FRAMEWORK = 'bootstrap3'
    LINK_SIZE = 'sm'
    SHOW_SINGLE_PAGE = False  # decide whether or not a single page returns pagination

    # Bcrypt algorithm hashing rounds
    BCRYPT_LOG_ROUNDS = 5

    SECRET_KEY = os.getenv('SECRET_KEY') or os.urandom(24)


class ProductionConfig(object):

    DEBUG = False
    TESTING = False