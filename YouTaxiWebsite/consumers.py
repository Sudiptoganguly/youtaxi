from channels.generic.websocket import AsyncWebsocketConsumer
import json


class UserConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    # Receive message from WebSocket
    async def receive(self, text_data):
        pass

    # Receive message from room group
    async def chat_message(self, event):
        pass





class DriverConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    # Receive message from WebSocket
    async def receive(self, text_data):
        pass

    # Receive message from room group
    async def chat_message(self, event):
        pass