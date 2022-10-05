from django.contrib import admin
from django.urls import path,include
app_name='app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('app.urls','app'),namespace='app')),#namespace is name of app
]