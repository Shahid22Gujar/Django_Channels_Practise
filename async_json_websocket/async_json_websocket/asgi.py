"""
ASGI config for async_json_websocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import app.routing
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'async_json_websocket.settings')

application = ProtocolTypeRouter(
    {
        'http':get_asgi_application(),
        'websocket':URLRouter(
            app.routing.websocket_urlpatterns
        )
    }
)
