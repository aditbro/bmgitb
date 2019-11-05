#!/bin/bash -x

. .env

until nc -z $DBHOST $DBPORT; do
	echo "Waiting mysql connection to $DBHOST:$DBPORT......"
	sleep 4
done

python manage.py makemigrations main
python manage.py migrate
echo "from django.contrib.auth.models import User; \
	User.objects.filter(username='${BMG_SUPADMIN}').exists() or \
	User.objects.create_superuser('$BMG_SUPADMIN', '', '${BMG_PASSWORD}')" | python manage.py shell

python manage.py $@
