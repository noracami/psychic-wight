# psychic-wight

# ToDo

---

# Environment
    $ python3 -V
    
    Python 3.4.0
    
    $ python3 -c "import django; print(django.get_version())"
    
    1.7.1

# Setup
    $ django-admin.py startproject psychicwight
    $ python3 manage.py startapp quiz

# basic command
    $ python3 manage.py makemigrations
    $ python3 manage.py sqlmigrate 'app' ####
    $ python3 manage.py migrate
    $ python3 manage.py runserver 0.0.0.0:8000
