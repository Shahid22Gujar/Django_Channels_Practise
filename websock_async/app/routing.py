from django.urls import path
from . import consumers
#websocket_urlpatterns is from consumers.py.i.e application ko websocket

websocket_urlpatterns=[
    path('ws/wsc/',consumers.MyWebsocketConsumer.as_asgi()),
    path('ws/awsc/',consumers.AsyncMyWebsocketConsumer.as_asgi()),
]