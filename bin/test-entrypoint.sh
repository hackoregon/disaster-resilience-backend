#!/bin/bash
export PATH=$PATH:~/.local/bin

# http://linuxcommand.org/lc3_man_pages/seth.html:
# -e  Exit immediately if a command exits with a non-zero status.
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
python -Wall manage.py collectstatic --noinput

python -Wall manage.py test --nomigrations --noinput --keepdb #--parallel