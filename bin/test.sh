#! /bin/bash
usage() { echo "Usage: $0 [-d] for a development test, [-p] for production test" 1>&2; exit 1; }

while getopts ":dp" opt; do
    case "$opt" in
        d)
          docker-compose -f development-docker-compose.yml run --entrypoint /code/bin/test-entrypoint.sh api_development -p 8000 --rm
          echo "Stopping test db container"
          docker stop tests_db_1
          echo "Removing test db container"
          docker rm tests_db_1
           ;;
        p)
          docker-compose -f production-docker-compose.yml run --entrypoint /code/bin/test-entrypoint.sh api_production -p 8000 --rm
          echo "Stopping test db container"
          docker stop tests_db_1
          echo "Removing test db container"
          docker rm tests_db_1
          ;;
        *)
          usage
          ;;
    esac
done
