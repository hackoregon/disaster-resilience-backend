#! /bin/bash

rm  manage.py
rm -rf dead_songs
rm -rf api

rm ./Backups/dead_songs.sql

docker-compose -f development-docker-compose.yml run db_development dropdb 'dead_songs'
