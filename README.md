# Start Project with django framework

## Create project initial file structure

If this is your first time using Django, you’ll have to take care of some initial setup. Namely, you’ll need to auto-generate some code that establishes a Django project – a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.

```
$ django-admin startproject mysite
```

## The development server

Let’s verify your Django project works. Change into the outer mysite directory, if you haven’t already, and run the following commands:DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_test_db',
        'USER': 'root',
        'PASSWORD': 'Nimna@123',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

```
$ python manage.py runserver
```

Now that the server’s running, visit ``http://127.0.0.1:8000/`` with your web browser. You’ll see a “Congratulations!” page, with a rocket taking off. It worked!


## Create stand alone component

```
 python3 manage.py startapp <component_name>
 ```

## Connect mysql to Django project

First you need to install mysql client `` pip install mysqlclient`` <br>

Add db datas to setting.py file
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_test_db',
        'USER': 'root',
        'PASSWORD': 'Nimna@123',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
```

After that create models and do migration

```
$ python3 manage.py makemigrations
$ python3 manage.py migrte
```
