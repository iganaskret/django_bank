import json
import asyncio
from random import randint
from time import sleep
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncConsumer
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer


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

# class NotifierConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print("connected", event)
#         await self.send({
#             "type": "websocket.accept"
#         })

#         await self.send({
#             "type": "websocket.send",
#             "text": "Hello"
#         })

#     async def websocket_receive(self, event):
#         print("receive", event)

#     async def websocket_disconnect(self, event):
#         print("disconnect", event)


# class NotifierConsumer(AsyncJsonWebsocketConsumer):

#     async def connect(self):
#         await self.accept()
#         while 1:
#             await asyncio.sleep(1)
#             await self.send_json("tick")
#             await asyncio.sleep(1)
#             await self.send_json(".....tock")

class NotifierConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("gossip", self.channel_name)
        print(f"Added {self.channel_name} channel to gossip")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("gossip", self.channel_name)
        print(f"Removed {self.channel_name} channel to gossip")

    async def user_gossip(self, event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")
