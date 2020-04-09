# Nolla.net tips

This document describes some useful things for developers.

## Environment vars

```bash
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = ''
MYSQL_PASSWORD = ''
MYSQL_DB = ''
RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
RECAPTCHA_OPTIONS = {'theme':'black'}
GOOGLE_API_KEY = ""
SECRET_KEY = ""
AZURE_BLOB_URI = ""
AZURE_ACCOUNT = ""
AZURE_CONTAINER = ""
AZURE_STORAGE_KEY = ""
FLASK_DEBUG = "1"
```


## Database usage
```bash
$ mysql -u root -p
mysql>SHOW DATABASES;
mysql>USE nolla;
mysql>SHOW TABLES;
mysql>SELECT * FROM users;
```

## Store new packages in requirements.txt
```bash
$ pip freeze > requirements.txt
```

## Flask sqlacodegen
```bash
$ flask-sqlacodegen  mysql://nolla:nolla@localhost:3306/nollatest --flask
```

## Flask CLI
```bash
$ export FLASK_APP=app/cli.py
```
```bash
$ flask alter_database
```

## Unit tests
```bash
$ python -m unittest -v tests/unit/tests.py
```

## Functional tests
```bash
$ pytest
```

or more specifically

```bash
$ pytest --setup-show tests/functional/test_users.py::test_home_page
```


## Leave venv
```bash
$ deactivate
```

