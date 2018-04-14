#! /bin/bash

set -euo pipefail

# Grab environment variables
. ./.env

# Remove sample files and database
echo "Removing the sample project..."
bin/remove-sample.sh

# Create django project and api app
echo "Creating new Django Rest Framework Project Scaffold..."
docker-compose -f development-docker-compose.yml run api_development /bin/bash -c "django-admin.py startproject $PROJECT_NAME . ; python manage.py startapp api"
echo "Removing temporary containers..."
docker stop $(docker ps -a -q  --filter name=db_development --format="{{.ID}}")
docker rm $(docker ps -a -q  --filter name=db_development --format="{{.ID}}")
docker rm $(docker ps -a -q  --filter name=api_development_run --format="{{.ID}}")

# Replace newly created settings with the example settings
echo "Configuring settings..."
rm $PROJECT_NAME/settings.py
cp ./bin/example-settings.py $PROJECT_NAME/settings.py

sed -i '' 's/\<EXAMPLE_PROJECT_NAME\>/'$PROJECT_NAME'/g' $PROJECT_NAME/settings.py

echo "Finished"
