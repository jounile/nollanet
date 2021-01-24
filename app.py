#!/usr/bin/env python3
import os

from app import app

if __name__ == '__main__':

    # Address setup
    host = os.environ.get('HOST', '0.0.0.0')
    port = os.environ.get('PORT', 8000)
    app.run(host=host, port=port)