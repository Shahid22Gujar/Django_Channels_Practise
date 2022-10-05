# import imp
# from channels.generic.websocket import WebsocketConsumer
# from asgiref.sync import async_to_sync
# from itsdangerous import json
# import json

# class TestConsumer(WebsocketConsumer):
#     #ws://
#     #connect send data from backend to frontend
#     def connect(self):
#         self.room_name = "test_consumer"
#         self.room_group_name="test_consumer_group"
#         async_to_sync(self.channel_layer.group_add(
#             self.room_name,self.room_group_name
#         ))
#         self.accept()
#         self.send(text_data=json.dumps({'status':'connected from django channel'}))#converting json to string



#     def receive(self):
#         pass
#     def disconnect(self):
#         pass
    
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio#For sleep method in async
import json
from asgiref.sync import async_to_sync#this convert asyc functiont to sync
from . models import *
class MySyncConsumer(SyncConsumer):
    '''This handler is called when client intially opens a connection and 
    is about to finish the Websocket handshake'''
    def websocket_connect(self,event):
        print("Websocket Connected..")
        print("Channel Layer....",self.channel_layer)#it return default channel layer name
        print("Channel Layer Name....",self.channel_name)#it return default channel name  
         #Name
        self.group_name=self.scope['url_route']['kwargs']['groupkaname']
        print("Group ka Name..",self.group_name)
        async_to_sync(self.channel_layer.group_add)(
        self.group_name,#group name
        self.channel_name)
        #self.send is used to establish connection
        #otherwise connection connect hoke disconnect hojayega
        self.send({
            'type':'websocket.accept'
        })
    # 
    #This handler is called when data receive from client ,sending through python data-dict
    def websocket_receive(self,event):
        print("Websocket Received..",event) #it print information received from client
        print("Message is..",event['text']) 
        print("Type Of Data Received..",type(event['text']))
        # data = json.loads(event['text'])#converting string to dict
        
        # print("Data....",data)
        # print("Type Of Data....",type(data))
        # print("Chat message",data['msg'])
        # #filter group_object
        # group = Group.objects.get(name=self.group_name)
        # #Create a New Chat object
        # chat=Chat(
        #     content=data['msg'],
        #     group=group
        # )
        # chat.save()
        print(self.scope['user'])
        # text['user']=self.scope['user'].username
        if self.scope['user'].is_authenticated:
            async_to_sync(self.channel_layer.group_send)(
            self.group_name,{
            'type':'chat.message',
            'message':event['text']
            }
            )
        else:
            self.send({
                'type':'websocket.send',
                'text':json.dumps({"msg":"Login Required"})
            })
    #This is our custom handler for chat.message
    def chat_message(self,event):# dot is replace by underscore here 
        print("Event...",event)
        print('Actual Message..',event['message'])
        print('Type Of Actual Message..',type(event['message']))
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })

        # self.send({
        #     'type':'websocket.send',
        #     'text':'Message sent to client'
        # })
        # for i in range(50):
        #     self.send({
        #         'type':'websocket.send',
        #         'text':json.dumps({'counter':i})
        #     })
        #     sleep(1)
    '''This handler is called either connectio to the client is loss,or 
    connection from client closing the connection
    the server closing the connection or loss of socket'''  
    def websocket_disconnect(self,event):
        print("Websocket disconnected..") 
        print("Channles layer...",self.channel_layer)
        print("Channles layer Name...",self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
        self.group_name,
        self.channel_name)
        raise StopConsumer()
class MyasyncConsumer(AsyncConsumer):
    '''This handler is called when client intially opens a connection and 
    is about to finish the Websocket handshake'''
    async def websocket_connect(self,event):
        print("Websocket Connected..")  
        print("Channel Layer....",self.channel_layer)#it return default channel layer name
        print("Channel Layer Name....",self.channel_name)#it return default channel name  
        self.channel_layer.group_add("programmers",self.channel_name)
        #self.send is used to establish connection
        #await is used for async
        await self.send({
            'type':'websocket.accept'
        })
    #This handler is called when data receive from client 
    async def websocket_receive(self,event):
        print("Websocket Received..",event) #it print information received from client
        print("Message is..",event['text'])
        # await self.send({
        #     'type':'websocket.send',
        #     'text':'Message sent to client'
        # })
        # for i in range(50):
        #     await self.send({
        #         'type':'websocket.send',
        #         'text':str(i)
        #     })
        #     await asyncio.sleep(1)
     #This is our custom handler for chat.message
    async def chat_message(self,event):# dot is replace by underscore here 
        print("Event...",event)
        print('Actual Message..',event['message'])
        print('Type Of Actual Message..',type(event['message']))
        await self.send({
            'type':'websocket.send',
            'text':event['message']
        })
    '''This handler is called either connectio to the client is loss,or 
    connection from client closing the connection
    the server closing the connection or loss of socket'''  
    async def websocket_disconnect(self,event):
        print("Websocket disconnected..") 
        print("Channles layer...",self.channel_layer)
        print("Channles layer Name...",self.channel_name)
        self.channel_layer.group_discard('programmers',
        self.channel_name)
        raise StopConsumer()