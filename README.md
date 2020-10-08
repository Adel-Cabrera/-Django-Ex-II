# Create virtual environment

python3 -m venv ./venv

# Activate virtual environment 

source ./venv/bin/activate

# Deactivate virtual environment 

deactivate

# Check dependencies

pip3 freeze

# Install Django

pip install django

# Install django pylint

pip install pylint-django

# Add to VSC -> settings.json

"python.linting.pylintArgs": [
    "--load-plugins=pylint_django",
    "--errors-only"

],

# Create django project through django-admin

django-admin startproject btre .

# Manage.py commands

python manage.py help

# Run server

python manage.py runserver

# Create Pages App

python manage.py startapp pages

# Coleccionar todos los archivos estáticos en una sola ruta (for deployment)

python manage.py collectstatic

# pgadmin

http://127.0.0.1/pgadmin4

# postgresql

psql

# Create database for the project

CREATE DATABASE btredb OWNER postgres;

# List postgresql datababases

\l 

# Exit psql

\q

# Install psycog2 and psycog2-binary to use postgresql in venv

pip install psycopg2

pip install psycopg2-binary

# Add postgres db to settings.py

# Run migrations

python manage.py migrate


___


# Create models

# Install Pillow for image handling

python -m pip install Pillow

# Create migrations for listing & realtor

python manage.py makemigrations

# To check the query to be inserted into DB -> Optional

python manage.py sqlmigrate listings 0001

# Run migrations

python manage.py migrate

# Create superuser for admin dashboard

python manage.py createsuperuser
 -> name: adel
 -> email: adel.cabrera.mesina@gmail.com
 -> password: my usual pass

 localhost:8000/admin/


