# Django Formset js
[![Build Status](https://travis-ci.com/chenuin/django-formset-js.svg?branch=master)](https://travis-ci.com/chenuin/django-formset-js)

Demo website with dynamic formset created by package django-formset-js

Original pacakge: https://pypi.org/project/django-formset-js/

## Deploy
Please clone this project first.
```sh
$ git clone https://github.com/chenuin/django-formset-js.git
```

#### Step1. Install
In my case, django 2.1.2 is installed. In order to style our form eazily, package `django-widget-tweaks` helps. It's optional if you don't mind interface.
```sh
# Method1: manually install
$ pip install django
$ pip install django-formset-js
$ pip install django-widget-tweaks

# Method2: install by requirements.txt
$ pip install -r requirements.txt
```

#### Step2. set up static files and database
The project adopts default settings "SQLite" as database.
```sh
$ python manage.py collectstatic
$ python manage.py makemigrations myapp
$ python manage.py migrate
```

#### Step3. Run
It's time to show our achievement!
```sh
$ python manage.py runserver
```
Open http://localhost:8000 in the browser to check it work properly

