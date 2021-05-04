"""
WSGI config for Mourse_courses project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mourse_courses.settings')

# from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
# application = DjangoWhiteNoise(get_wsgi_application())
