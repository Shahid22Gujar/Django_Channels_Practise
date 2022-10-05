from channels.generic.websocket import JsonWebsocketConsumer,AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
from app.models import Group,Chat
#as we cannot use async function in sync consumer
#Note django ORM are sync functions
class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    
    def connect(self):
        print("Websocket Connected ....")
        print("Channel Name...",self.channel_name)
        print("Channel Layer...",self.channel_layer)
        self.group_name=self.scope['url_route']['kwargs']['group_name']
    
       
        print("Group Name...",self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name 
        ) # one group has multiple channel layers
        self.accept() # To accept connection
    
    def receive_json(self,content,**kwargs):
        print("Receiving Content",content)
        group=Group.objects.get(name=self.group_name)
        #checking whether user is logged in or not
        
        if self.scope['user'].is_authenticated:
            chat=Chat(
                content=content['msg'],
                group=group
            )
            chat.save()
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                'type':'chat.message', # this is event for client
                'message':content['msg']
            })
        else:
            self.send_json({
                'message':'Login Required'
            })
        
    def chat_message(self,event):
        print("Event ...",event)
        self.send_json({
            'message':event['message']
        })
    
    def disconnect(self):
        pass