from django.contrib import admin
from app.models import Group,Chat

# Register your models here.
admin.site.register((Group,Chat))