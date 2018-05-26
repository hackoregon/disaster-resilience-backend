#! /bin/bash


# http://linuxcommand.org/lc3_man_pages/seth.html:
# -e  Exit immediately if a command exits with a non-zero status.
set -e

echo Debug: $DEBUG

# Pull in environment variables values from AWS Parameter Store, and preserve the exports
source /code/bin/get-ssm-parameters.sh

# Temporary troubleshooting
echo "from entrypoint script DJANGO_SECRET_KEY value is " $DJANGO_SECRET_KEY

python -Wall manage.py collectstatic --noinput


gunicorn $PROJECT_NAME.wsgi -c gunicorn_config.py