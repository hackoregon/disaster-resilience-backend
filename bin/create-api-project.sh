#! /bin/bash

set -euo pipefail

# Grab environment variables
. ./.env

# Remove sample files and database
bin/remove-sample.sh

# Create django project and api app
docker-compose -f development-docker-compose.yml run api_development /bin/bash -c "django-admin.py startproject $PROJECT_NAME . ; python manage.py startapp api"
docker stop $(docker ps -a -q  --filter ancestor=db_development --format="{{.ID}}")

# Replace newly created settings with the example settings
rm $PROJECT_NAME/settings.py
cp ./bin/example-settings.py $PROJECT_NAME/settings.py

sed -i '' 's/\<EXAMPLE_PROJECT_NAME\>/'$PROJECT_NAME'/g' $PROJECT_NAME/settings.py
