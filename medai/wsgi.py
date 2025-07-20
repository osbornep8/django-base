"""
<<<<<<< HEAD
WSGI config for medai project.
=======
WSGI config for movies project.
>>>>>>> fbda72df505c152eba1f074ba8edb5a57de0b6d0

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medai.settings")

application = get_wsgi_application()
