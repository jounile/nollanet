# Nolla.net tips

This document describes some useful things for developers.

## Environment vars

```bash
FLASK_CONFIGURATION = "development"
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
```

# Use development configuration
```bash
$ source ./env.dev
```

## Store new packages in requirements.txt
```bash
$ pip freeze > requirements.txt
```


## Install test utility

```bash
$ pip install pytest-docker-compose
```

## Functional tests
```bash
$ pytest
```

or more specifically

```bash
$ pytest --setup-show -v tests/functional/test_frontpage.py::test_frontpage
```


## Leave venv
```bash
$ deactivate
```

