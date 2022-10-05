from django.urls import path
from app.views import index
urlpatterns = [
    path('<str:group_name>/', index,name="home"),
]