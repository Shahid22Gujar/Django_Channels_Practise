from django.urls import path
from . import consumers
websocket_urlpatterns=[
    path('ws/jwc/<str:group_name>/',consumers.MyJsonWebsocketConsumer.as_asgi())
]