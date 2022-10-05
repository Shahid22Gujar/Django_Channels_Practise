#Topic - Generic Consumer - WebsocketConsumer and 
#AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer

class MyWebsocketConsumer(WebsocketConsumer):
    #This handler is called when client intially opens a connection and is about
    #the Websocket handshake

    def connect(self):
        print('Websocket Connected..')
        self.accept()
        # self.close()#For rejecting connection forcefully

    #This handler is called when data received from client
    def receive(self,text_data=None,bytes_data=None):
        print('Message Received from client..',text_data)
        #send data to client
        self.send(text_data="Message from server to Client")
        #sending bytes frame
        # self.send(bytes_data=data)
        self.close(code=4142)

    #This handler is called when either connection to the client is lost,either
    #from the client losing the connection ,the server closing the connection,
    #the server closing the connnection,or loss of the socket
    def disconnect(self,close_code):
        print('Websocket disconnected..',close_code)
    

class AsyncMyWebsocketConsumer(AsyncWebsocketConsumer):
    #This handler is called when client intially opens a connection and is about
    #the Websocket handshake

    async def connect(self):
        print('Websocket Connected..')
        await  self.accept()
        # self.close()#For rejecting connection forcefully

    #This handler is called when data received from client
    async def receive(self,text_data=None,bytes_data=None):
        print('Message Received from client..',text_data)
        #send data to client
        await self.send(text_data="Message from server to Client")
        #sending bytes frame
        # self.send(bytes_data=data)
        # self.close(code=4142)

    #This handler is called when either connection to the client is lost,either
    #from the client losing the connection ,the server closing the connection,
    #the server closing the connnection,or loss of the socket
    async def disconnect(self,close_code):
        print('Websocket disconnected..',close_code)
    
