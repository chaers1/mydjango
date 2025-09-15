"""
项目如果运行在asgi兼容的web服务器上的入口
ASGI config for django_keshihua project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_keshihua.settings")

application = get_asgi_application()
