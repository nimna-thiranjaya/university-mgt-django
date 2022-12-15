# Start Project with django framework

## Create project initial file structure

If this is your first time using Django, you’ll have to take care of some initial setup. Namely, you’ll need to auto-generate some code that establishes a Django project – a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.

```
$ django-admin startproject mysite
```

## The development server

Let’s verify your Django project works. Change into the outer mysite directory, if you haven’t already, and run the following commands:

```
$ python manage.py runserver
```

Now that the server’s running, visit ``http://127.0.0.1:8000/`` with your web browser. You’ll see a “Congratulations!” page, with a rocket taking off. It worked!


## Create stand alone component

```
 python3 manage.py startapp <component_name>
 ```
