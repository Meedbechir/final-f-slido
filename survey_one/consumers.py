from channels.generic.websocket import AsyncWebsocketConsumer
import json

class SurveyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket connection established.")
        await self.accept()

    async def disconnect(self, close_code):
        print(f"WebSocket connection closed with code {close_code}.")

    async def receive(self, text_data):
        print("Message received:", text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print("Sending message back to client:", message)
        await self.send(text_data=json.dumps({
            'message': message
        }))
