#!/bin/sh
python manage.py migrate
python manage.py loaddata fixtures/heroku.json
exec "$@"
