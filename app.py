#!/usr/bin/env python3
import os

import logging
from logging.handlers import RotatingFileHandler

from app import app

if __name__ == '__main__':
    app.debug = False
    host = os.environ.get('HOST', '0.0.0.0')
    port = os.environ.get('PORT', 8080)
    app.run(host=host, port=port)