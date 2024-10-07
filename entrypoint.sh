#!/bin/sh

# Wait for the database to be ready (optional)
# ./wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Database is up"

# Run migrations and create initial data
python manage.py makemigrations
python manage.py migrate
python manage.py create_initial_data

# Start the server
exec python manage.py runserver 0.0.0.0:8000