import json
import asyncio
from random import randint
from time import sleep
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncConsumer
from channels.db import database_sync_to_async


# class NotifierConsumer(WebsocketConsumer):
#     def connect(self, event):
#         # accept incoming connection from the browser(client)
#         self.accept()
#         # message to the connection as json object
#         for i in range(1000):
#             # send method
#             self.send(json.dumps({
#                 # message key
#                 'message': randint(1, 10)
#             }))
#             sleep(2)

class NotifierConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        # print(self.scope)
        await self.send({
            "type": "websocket.accept"
        })

        #other_user = self.scope['url_route']
        await self.send({
            "type": "websocket.send",
            "text": "Hello"
        })

    async def websocket_receive(self, event):
        print("receive", event)
        #print(f'EVENT {event}')

    async def websocket_disconnect(self, event):
        print("disconnect", event)
