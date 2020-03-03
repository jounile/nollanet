#!/usr/bin/env python3
import os
import logging
from logging.handlers import RotatingFileHandler

from app import app

if __name__ == '__main__':

    # Debug setup
    app.debug = False

    # Logger setup
    LOG_FILENAME = 'nollanet.log'
    #LOG_LEVEL = logging.DEBUG
    LOG_LEVEL = logging.ERROR
    #LOG_LEVEL = logging.INFO

    formatter = logging.Formatter( "%(asctime)s | %(pathname)s:%(lineno)d | %(funcName)s | %(levelname)s | %(message)s ")
    handler = RotatingFileHandler(LOG_FILENAME, maxBytes=10000000, backupCount=5)
    handler.setLevel(LOG_LEVEL)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    # Address setup
    host = os.environ.get('HOST', '0.0.0.0')
    port = os.environ.get('PORT', 8000)
    app.run(host=host, port=port)