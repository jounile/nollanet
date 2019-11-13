# Nolla.net

## Create a virtualenv (Mac & WSL)
```bash
$ pip install virtualenv
$ virtualenv venv
$ virtualenv -p /usr/bin/python2.7 venv
$ export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2.7
$ source venv/bin/activate
```

## Install modules in venv
```bash
$ pip install --upgrade pip
$ sudo apt-get install python3-dev
$ pip install -r requirements.txt
```

## Environment vars
```bash
$ . env.sh
```

## Run locally
```bash
$ python app.py
```

## Tests
```bash
$ python tests.py
```

## Deactivate virtual environment
```bash
$ deactivate
```