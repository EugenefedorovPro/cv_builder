#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

## for development only
python manage.py runserver 0.0.0.0:8002 --nothreading
## alternative for development
#gunicorn monitor_project.wsgi:application --bind 0.0.0.0:8002 --workers=2 --timeout=300 --reload
