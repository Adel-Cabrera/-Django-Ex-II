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