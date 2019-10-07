# Introduction to Flask

## Create a virtualenv (Mac & WSL)
```bash
$ pip install virtualenv
$ virtualenv venv
$ virtualenv -p /usr/bin/python3.6 venv
$ export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6
$ source venv/bin/activate
```

## Install modules in venv
```bash
$ pip install --upgrade pip
$ sudo apt-get install python3-dev
$ pip install -r requirements.txt
```

Add to environment vars

## Database connection params
```text
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = ''
MYSQL_PASSWORD = ''
MYSQL_DB = ''
MYSQL_PORT = 3306
```

## ReCaptcha
```bash
RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
RECAPTCHA_OPTIONS = {'theme':'black'}
```

## Youtube
```bash
GOOGLE_API_KEY = ""
```

## Session handling
```bash
SECRET_KEY = ""
```

## Images and videos
```bash
AZURE_BLOB = ""
```

## Facebook
Add this in the /app/mod_facebook/facebook.json file
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

## Nginx in Docker
```bash
$ docker build -t mynginx -f Dockerfile-nginx .
$ docker run --name mynginx -p 80:80 -d mynginx
```

http://localhost/static/tn/6134_50.jpg

is reverse proxied to

http://nolla.net/mediagalleria/tn/6134_50.jpg

## Run locally
```bash
$ python app.py
```

## Store new packages in requirements.txt
```bash
$ pip freeze > requirements.txt
```

## Deactivate virtual environment
```bash
$ deactivate
```


## Flask CLI
```bash
$ export FLASK_APP=app/cli.py
```
```bash
$ flask alter_database
```

