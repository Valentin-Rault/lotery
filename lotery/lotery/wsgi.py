"""
WSGI config for lotery project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
# wsgi.py
import os

from django.core.wsgi import get_wsgi_application

from aiodjango import get_aio_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example.settings')

# Build WSGI application
# Any WSGI middleware would be added here
application = get_wsgi_application()

# Build aiohttp application
app = get_aio_application(application)
