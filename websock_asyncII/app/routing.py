from django.urls import path
from . import consumers

websocket_urlpatterns=[
    path('ws/wsc/<str:group_name>/',consumers.MyWebsocketConsumer.as_asgi()),
    # spath('ws/awsc/',consumers.AsyncMyWebsocketConsumer.as_asgi()),
]