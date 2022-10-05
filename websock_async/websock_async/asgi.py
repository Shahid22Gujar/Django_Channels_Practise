"""
ASGI config for websock_async project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websock_async.settings')
#For ASGI Configuration
from channels.routing import ProtocolTypeRouter,URLRouter
import app.routing

application=ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(
        app.routing.websocket_urlpatterns
    ),

})

# application = get_asgi_application() 
#If we donot comment application then it will give error channels handle asgi
#not websocket so we must comment or remove ths application with
#ProtocolTypeRouter
