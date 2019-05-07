#!/bin/sh -x

. .env

until nc -z database 3306; do
	sleep 3
done

python manage.py makemigrations main
python manage.py migrate
echo "from django.contrib.auth.models import User; \
	User.objects.filter(username='admin').exists() or \
	User.objects.create_superuser('$BMG_SUPADMIN', '', '${BMG_PASSWORD}')" | python manage.py shell

python manage.py $@
