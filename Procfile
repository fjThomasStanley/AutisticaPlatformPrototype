release: python manage.py migrate --noinput
web: gunicorn skeleton.apps.Main.wsgi --log-file=-
