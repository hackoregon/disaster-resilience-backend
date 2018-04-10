# Example Geo-Capable Django RestFramework using Docker

Simple Example Repo to quickstart a DRF API within a Docker Container

Allows for multiple environments to run API, through series of docker-compose files. You should be able to replace the Django Code, making a few updates and get this running

## Main Parts of Repo:

DOCKER related:

* env.sample - A sample env file to setup environmental variables
* bin directory - directory to store your startup and entrypoint scripts.
* Backups directory - directory will store any database backups to restore into the local database Container, also restore script
* Docker-Compose Files -  4 files which compose containers and networking for each environment:
    * local-docker-compose.yml - This is a local dev environment, will spin up a local api container connecting with a local db. It will run the Django Dev Server with the DEBUG variable set to True.
    * staging-docker-compose.yml - This is set to run a production-like environment, creating a api container running with gunicorn server, and green database pooling. It removes the local development from the stack, connecting to a remote database for which the variables/creds are entered into the staging vars in the .env file
    * travis-docker-compose.yml - Deploy version of docker-compose file
    * testing-docker-compose.yml - configures testing version of the API
* DOCKERFILEs:
  * DOCKERFILE.db.development - The DOCKERFILE for local database container
  * DOCKERFILE.api.development - The DOCKERFILE for local api container
  * DOCKERFILE.api.staging - The DOCKERFILE for local api container

API Related:

* gunicorn_config.py - Config file for the gunicorn server


## Getting Started

First you will want to setup your .env

### .env file

1. `cp env.sample .env` in the root of the repo (this file is already in the .gitignore, so you should not have to worry about it being checked into github)

2. To begin with setup you local variables, ignoring the staging ones at this time:

```
PROJECT_NAME=<What you want to name the project>
# keep as true to run the django dev server
DEBUG=True

# the database superuser name - this is the default
DEVELOPMENT_POSTGRES_USER=postgres

# the database name the API will connect to - "dbname" in most PostgreSQL command-line tools
DEVELOPMENT_POSTGRES_NAME=<your_database_name>

# *service* name (*not* image name) of the database in the Docker network
DEVELOPMENT_POSTGRES_HOST=db_development

# port the database is listening on in the Docker network
DEVELOPMENT_POSTGRES_PORT=5432

# password for the PostgreSQL database superuser in the database container
DEVELOPMENT_POSTGRES_PASSWORD=sit-down-c0mic

# Django secret key in the API container
DEVELOPMENT_DJANGO_SECRET_KEY=r0ck.ar0und.the.c10ck
```

3. 
