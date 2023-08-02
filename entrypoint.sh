#!/bin/sh

set -e

host="$1"
shift
cmd="$@"

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z "$DB_HOST" "$DB_PORT"; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Add paths to manage.py accordingly
python /code/dcrm/manage.py flush --no-input
python /code/dcrm/manage.py migrate

# Create admin user
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password') if not User.objects.filter(username='admin').exists() else print('Admin user already exists')" | python /code/dcrm/manage.py shell

# Starting Django server
python /code/dcrm/manage.py runserver 0.0.0.0:8000

exec "$@"
