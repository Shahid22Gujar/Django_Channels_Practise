
#Topic-Generic Consumer - WebsocketConsumer and AsyncWebsocketConsumer
#ChatApp

import json
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from time import sleep
import asyncio #async sleep
#channel layer ka sabai function async hote hai 
#sync me use ke liye sync me convert kar rahe hai
from asgiref.sync import async_to_sync

class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print('Websocket Connected..')
        print("Channel Layer...",self.channel_layer)
        print("Channel Name..",self.channel_name)
        self.group_name=self.scope['url_route']['kwargs']['groupkaname']
        print("Group Name..",self.group_name)
        '''self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )'''
        #Now converting commented code to sync
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def receive(self,text_data=None,byte_data=None):
        print("Message received from Client...",text_data)
        #converting received json data to python native data 
        data=json.loads(text_data)#it convert to dictionary
        print("Data...",data)
        message=data['msg']#accessing through key
        print(message)
        #sending msg to channel
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type':'chat.message',#chat.message is handler so need to write
                #chat.message => chat_message in handeler below
                'message':message
            }
            
        )
    def chat_message(self,event):
        print("Event....",event)
        self.send(text_data=json.dumps({
            'msg':event['message']
        }))
        
        
        #send data to client
        # for i in range(20):
        #     print(i)
        #     #text_data need string so casting to string
        #     self.send(text_data=str(i))#as it need string so converting
        #     sleep(1)

    def disconnect(self,close_code):
        print('Websocket disconnected..',close_code)
        print("Channel Layer...",self.channel_layer)
        print("Channel Name..",self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name ,
            self.channel_name
        )

class AsyncMyWebsocketConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print('Websocket Connected..')
        print("Channel Layer...",self.channel_layer)
        print("Channel Name..",self.channel_name)
        self.group_name=self.scope['url_route']['kwargs']['groupkaname']
        print("Group Name..",self.group_name)
        '''self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )'''
        #Now converting commented code to sync
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def receive(self,text_data=None,byte_data=None):
        print("Message received from Client...",text_data)
        data=json.loads(text_data)#it convert to dictionary
        print("Data...",data)
        message=data['msg']#accessing through key
        print(message)
        #sending msg to channel
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type':'chat.message',#chat.message is handler so need to write
                #chat.message => chat_message in handeler below
                'message':message
            }
            
        )
        #send data to client
        # for i in range(20):
        #     print(i)
        #     #text_data need string so casting to string
        #     self.send(text_data=str(i))#as it need string so converting
        #     await asyncio.sleep(1)#await for asycn

    async def chat_message(self,event):
        print("Event....",event)
        await self.send(text_data=json.dumps({
            'msg':event['message']
        }))

    async def disconnect(self,close_code):
        print('Websocket disconnected..',close_code)
        print("Channel Layer...",self.channel_layer)
        print("Channel Name..",self.channel_name)
        await self.channel_layer.group_discard(
            self.group_name ,
            self.channel_name
        )