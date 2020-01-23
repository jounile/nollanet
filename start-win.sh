#!/bin/bash

# Create virtualenv
pip install virtualenv
virtualenv venv
virtualenv -p /usr/bin/python3.7 venv
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.7
source venv/bin/activate

# Install python modules
pip install --upgrade pip
sudo apt-get install python3-dev
pip install mysqlclient==1.4.2.post1
pip install -r requirements.txt

# Export environment variables
. env.sh

# Start nollanet app
python app.py