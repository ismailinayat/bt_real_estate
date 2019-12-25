#!/usr/bin/env python
"""Django's command-line utility for administrative tasks. This file was created when we ran command "django-admin startproject btre". And this is what we will use from
    now on to manage our app instead of using "django-admin" which we did used to start our project. We will use "manage.py" for doing things like migrations, running server,
    creating users etc. """
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'btre.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
