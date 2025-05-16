#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn --bind=https://hobbysite-f-20-g0gqa7acascyhed2.southeastasia-01.azurewebsites.net/ --timeout 600 hobbysite.wsgi --access-logfile '-' --error-logfile '-'