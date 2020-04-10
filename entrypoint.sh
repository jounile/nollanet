#!/bin/sh

echo "Waiting for database..."
while ! nc -z $MYSQL_HOST $MYSQL_PORT; do
  sleep 0.5
done
echo "Database started"

echo "Database init"
python manage.py
echo "Database init finished"

exec "$@"