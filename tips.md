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
AZURE_BLOB = ""
```

## Facebook tokens
```bash
{
    "app": {
        "secret": "", 
        "id": ""
    }, 
    "user": {
        "long_token": "", 
        "short_token": ""
    }, 
    "page": {
        "token": "", 
        "id": ""
    }
}
```

## Database usage
```bash
$ mysql -u root -p
mysql>SHOW DATABASES;
mysql>USE nolla;
mysql>SHOW TABLES;
mysql>SELECT * FROM users;
```

## phpMyAdmin in Docker
```bash
$ docker pull phpmyadmin/phpmyadmin
$ docker run --name myadmin -d -e PMA_HOST=docker.for.mac.localhost -e PMA_PORT=3306 -p 8000:80 phpmyadmin/phpmyadmin
```

http://localhost:8000

Username: root

Password: root


## Store new packages in requirements.txt
```bash
$ pip freeze > requirements.txt
```


## Flask CLI
```bash
$ export FLASK_APP=app/cli.py
```
```bash
$ flask alter_database
```
