#!/bin/sh

echo "Waiting for database..."

while ! nc -z $MYSQL_HOST $MYSQL_PORT; do
  sleep 0.5
done

echo "Database started"

echo "Ensuring db init"

export FLASK_APP=app.py
flask shell << HERE
from app import db
db.create_all()
HERE

exec "$@"