"""
ASGI config for jsonwebsocket_chatapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import app.routing
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
#AuthMiddlewareStack is used for authentication checking websocket
from channels.auth import AuthMiddlewareStack 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jsonwebsocket_chatapp.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(URLRouter(
        app.routing.websocket_urlpatterns
    ))
})
