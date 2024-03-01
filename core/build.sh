#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python3 manage.py collectstatic --no-input
python3 manage.py migrate

# python3 manage.py runserver



