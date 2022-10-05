#Topic-Generic Consumer - WebsocketConsumer and AsyncWebsocketConsumer
#ChatApp with Dynamic Group Name




from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from time import sleep
import asyncio #async sleep

class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print('Websocket Connected..')
        self.accept()

    def receive(self,text_data=None,byte_data=None):
        print("Message received from Client...",text_data)
        #send data to client
        for i in range(20):
            print(i)
            #text_data need string so casting to string
            self.send(text_data=str(i))#as it need string so converting
            sleep(1)

    def disconnect(self,close_code):
        print('Websocket disconnected..',close_code)

class AsyncMyWebsocketConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print('Websocket Connected..')
        await self.accept()

    async def receive(self,text_data=None,byte_data=None):
        print("Message received from Client...",text_data)
        #send data to client
        for i in range(20):
            print(i)
            #text_data need string so casting to string
            self.send(text_data=str(i))#as it need string so converting
            await asyncio.sleep(1)#await for asycn

    async def disconnect(self,close_code):
        print('Websocket disconnected..',close_code)
