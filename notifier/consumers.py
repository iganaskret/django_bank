from channels.generic.websocket import AsyncJsonWebsocketConsumer


class NotifierConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("notification", self.channel_name)
        print(f"Added {self.channel_name} channel to notification")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notification", self.channel_name)
        print(f"Removed {self.channel_name} channel to notification")

    async def user_notification(self, event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")
