from django.shortcuts import render
from app.models import Group,Chat

# Create your views here.
def index(request,group_name):
    chats=[]
    group=Group.objects.filter(name=group_name).first()
    if not group:
        Group.objects.create(name=group_name)
    else:
        chats=Chat.objects.filter(group=group)
    context={'group_name':group_name,'chats':chats}
    return render(request,'app/index.html',context)