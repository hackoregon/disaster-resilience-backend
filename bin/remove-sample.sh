#! /bin/bash

if [ -f ./manage.py ]; then
    rm -rf manage.py
fi
#
if [ -d ./dead_songs ]; then
    rm -rf dead_songs
fi

if [ -d ./api ]; then
    rm -rf api
fi

if [ -f ./Backups/dead_songs.sql ]; then
    rm ./Backups/dead_songs.sql
fi
