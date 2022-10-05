"""
ASGI config for django_chaneel_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import imp
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.urls import path
from django.core.asgi import get_asgi_application
import home.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_chaneel_project.settings')
from channels.auth import AuthMiddlewareStack

# application = get_asgi_application()
# ws_patterns = [
# path('/ws/test/',TestConsumer),
# ]
application=ProtocolTypeRouter({'http':get_asgi_application(),
'websocket':AuthMiddlewareStack(URLRouter(home.routing.websocket_urlpatterns)) 
})