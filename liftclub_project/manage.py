#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Set the DJANGO_SETTINGS_MODULE environment variable to specify the settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'liftclub_project.settings')
    try:
         # Import the execute_from_command_line function from the Django core management module
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Handle ImportError if Django is not installed or not available on PYTHONPATH
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Execute Django management commands from the command line arguments
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # If this script is executed directly, call the main function
    main()
