"""
<<<<<<< HEAD
ASGI config for medai project.
=======
ASGI config for movies project.
>>>>>>> fbda72df505c152eba1f074ba8edb5a57de0b6d0

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medai.settings")

application = get_asgi_application()
