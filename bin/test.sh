#! /bin/bash
usage() { echo "Usage: $0 [-d] for a development test, [-p] for production test" 1>&2; exit 1; }

if [ $# == 0 ]; then usage; fi

while getopts ":dp" opt; do
    case "$opt" in
        d)
          docker-compose -f development-docker-compose.yml -p tests run --entrypoint /code/bin/test-entrypoint.sh  -p 8000 --rm api_development
          echo "Stopping test db container"
          docker stop tests_db_development_1
          echo "Removing test db container"
          docker rm tests_db_development_1
           ;;
        p)
          echo "still needs building"
          ;;
        *)
          usage
          ;;
    esac
done
