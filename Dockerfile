FROM django:1.8.6-python2
ADD . /usr/src/app
EXPOSE 8000
CMD python manage.py runserver