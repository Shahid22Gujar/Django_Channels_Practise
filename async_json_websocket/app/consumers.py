#Topic AsyncJsonWebsocketConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
import asyncio # this is used for sleep as we are using async
class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("Websocket connected")
        await self.accept() # to accept connection
        # await self.close() # to reject connection
    
    async def receive_json(self,content,**kwargs):
        print("Received Message .....",content)
        print("Type of Message Received..",type(content))
        for i in range(20):
            await self.send_json({
                "message":str(i)
            })
            await asyncio.sleep(1) #await should be used when using async
    async def disconnect(self,close_code):
        print("Websocket Disconnected...",close_code)
        