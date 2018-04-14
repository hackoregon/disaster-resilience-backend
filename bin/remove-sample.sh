#! /bin/bash

if [ -f ./manage.py ]; then
    echo "removing manage.py"
    rm -rf manage.py
fi
#
if [ -d ./dead_songs ]; then
    echo "removing django project folder"
    rm -rf dead_songs
fi

if [ -d ./api ]; then
    echo "removing api app folder"
    rm -rf api
fi

if [ -f ./Backups/dead_songs.sql ]; then
    echo "removing sanmple db backup"
    rm ./Backups/dead_songs.sql
fi

if [ "docker ps -a -q -f ancestor=db_development --format=\"{{.ID}}\"" ]; then
  echo "removing db container"
  docker stop $(docker ps -a -q  --filter ancestor=db_development --format="{{.ID}}")
  docker rm $(docker ps -a -q  --filter ancestor=db_development --format="{{.ID}}")
fi

if [ "docker ps -a -q -f name=api_development --format=\"{{.ID}}\"" ]; then
  echo "removing api container"
  docker stop $(docker ps -a -q  --filter name=api_development --format="{{.ID}}")
  docker rm $(docker ps -a -q  --filter name=api_development --format="{{.ID}}")
fi
