#!/usr/bin/env bash

# Apply database migrations
echo "Apply database migrations"
./bin/wait-for-it.sh -t 5 db:5432 -- echo "β DB is up"

COUNTER=0

while
  ./manage.py migrate --noinput
  M=$?
  [[ $M -eq 1 ]] && [ $COUNTER -lt 6 ]
do
  ((COUNTER++))
  echo "β οΈ couldn't migrate, tyring again shortly"
  echo "    (attempt $COUNTER of 5)"
  sleep 3
done

echo "π§β Creating superuser"
./manage.py createsuperuser --noinput

echo "π₯ Collecting static files"
./manage.py collectstatic --noinput

# TODO: move to separate dev scripts or check for env variable or something
#echo "πΊοΈ Loading Geography Types"
#./manage.py loaddata geostuff/region-types.json
#
#./manage.py load_geogs

echo "π Starting..."
./manage.py runserver 0.0.0.0:8000

exec "$@"
