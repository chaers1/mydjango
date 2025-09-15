#!/usr/bin/env python   一个使用各种法师管理django项目的额命令行工具  启动项目的命令python manage。py migrate
"""Django's command-line utility for administrative tasks."""
# !/usr/bin/env python
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_keshihua.settings')

    try:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


if __name__ == '__main__':
    main()
