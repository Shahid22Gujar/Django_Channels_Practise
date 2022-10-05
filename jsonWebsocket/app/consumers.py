"""Topic - Generic Consumer- JsonWebSocketConsumer and 
And AsyncJsonWebsocket Consumer
"""
from channels.generic.websocket import JsonWebsocketConsumer,AsyncJsonWebsocketConsumer
from time import sleep


class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    """This handler is called when client intially
    opens a connection and is about to finish the Websocket handshake"""
    def connect(self):
        print("Websocket connected.......")
        self.accept() #without this connection disconnected after connecting
        # self.close() # this is used to reject connection
    
    """This handler is called when data received from clinet
    with decoded JSON content"""
    def receive_json(self, content, **kwargs):
        print("Message received from client....",content)
        print("Type of message received from client",type(content))
        # self.send_json({'This message from server':'hi'})
        for i in range(20):
            self.send_json({'message':str(i)})
            sleep(1)

        #self.close #=>to forcefully reject connection
    
    """This handler is called when either connection to the client
    is lost,either from the client closing the connection,or loss of socket"""
    def disconnect(self, close_code):
        print("Websocket disconnected..",close_code)

class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    """This handler is called when client intially
    opens a connection and is about to finish the Websocket handshake"""
    async def connect(self):
        print("Websocket connected.......")
        await self.accept() #without this connection disconnected after connecting
        # self.close() # this is used to reject connection
    
    """This handler is called when data received from clinet
    with decoded JSON content"""
    async def receive_json(self, content, **kwargs):
        print("Message received from client....",content)
        print("Type of message received from client",type(content))
        await self.send_json({'This message from server':'hi'})
        # await self.close()
    
    """This handler is called when either connection to the client
    is lost,either from the client closing the connection,or loss of socket"""
    async def disconnect(self, close_code):
        print("Websocket disconnected..",close_code)