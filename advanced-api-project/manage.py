#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')
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
from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer

# create objects
a = Author.objects.create(name='Test Author')
b = Book.objects.create(title='My Book', publication_year=2020, author=a)

# serialize author (nested books included)
serializer = AuthorSerializer(a)
print(serializer.data)

# attempt to create book with a future publication year — should raise validation error when using serializer
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser

bad_data = {'title': 'Future Book', 'publication_year': 9999, 'author': a.id}
serializer = BookSerializer(data=bad_data)
if not serializer.is_valid():
    print(serializer.errors)