#!/bin/bash
export PATH=$PATH:~/.local/bin

set -e

export PGPASSWORD=$POSTGRES_PASSWORD
until psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -p "$POSTGRES_PORT" -d postgres -c '\q'
do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 5
done

>&2 echo "Postgres is up"

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

python manage.py test --nomigrations --noinput --keepdb #--parallel