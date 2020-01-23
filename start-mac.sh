#!/bin/bash

# Create virtualenv
python3 -m pip install --upgrade pip
pip3 install virtualenv
virtualenv -p /usr/local/bin/python3 venv
source venv/bin/activate

# Install python modules
pip install --upgrade pip
brew install openssl
brew install mysql
pip3 install mysqlclient
pip install -r requirements-mac.txt

# Export environment variables
. env.sh

# Start nollanet app
python app.py