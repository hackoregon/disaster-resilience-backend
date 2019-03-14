#! /bin/bash
usage() { echo "Usage: $0 [-d] for a development build, [-p] for a production build" 1>&2; exit 1; }

if [ $# == 0 ]; then usage; fi

while getopts ":dpb" opt; do
    case "$opt" in
        d)
          docker-compose -f development-docker-compose.yml up
          ;;
        p)
          docker-compose -f production-docker-compose.yml up
          ;;
        b)
          docker-compose -f development-docker-compose.yml run --entrypoint bash -p 8000:8000 db_development
          ;;
        *)
          usage
          ;;
    esac
done

# fix ownership
echo "Fixing ownership on Linux"
if [ `uname -s` = "Linux" ]
then
  ls -l
  echo "sudo chown -R `id -u $USER`:`id -g $USER` ."
  sudo chown -R `id -u $USER`:`id -g $USER` .
  ls -l
fi