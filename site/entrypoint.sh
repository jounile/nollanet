#!/bin/sh

echo "Waiting for database..."

while ! nc -z $MYSQL_HOST $MYSQL_PORT; do
  sleep 0.5
done

echo "Database started"

#python manage.py flush --no-input
#python manage.py migrate
#python manage.py collectstatic --no-input --clear
#python manage.py createsuperuser --no-input --email admin@example.invalid --username admin
#python manage.py loaddata accounts.json transactions.json

exec "$@"