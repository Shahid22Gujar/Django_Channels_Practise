from django.contrib import admin
from . models import Chat,Group

# Register your models here.
@admin.register(Chat)
class Chat(admin.ModelAdmin):
    list_display=['id','message','timestamp','group']

@admin.register(Group)
class Chat(admin.ModelAdmin):
    list_display=['id','groupname']