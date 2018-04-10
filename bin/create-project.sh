#! /bin/bash

rm  manage.py
rm -rf dead_songs

docker-compose -f development-docker-compose.yml run api_development django-admin.py startproject $PROJECT_NAME .

rm $PROJECT_NAME/settings.py
cp ./bin/settings.py $PROJECT_NAME/settings.py
