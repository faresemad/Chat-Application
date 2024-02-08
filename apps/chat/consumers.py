import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model

from apps.chat.models import Message, Room

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_id = None
        self.room_group_name = None
        self.user = None

    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = f"chat_{self.room_id}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        author_id = self.scope["user"].id
        await sync_to_async(self.save_message)(message, author_id)
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message, "author_id": author_id}
        )

    async def chat_message(self, event):
        message = event["message"]
        author_id = event["author_id"]
        await self.send(text_data=json.dumps({"message": message, "author": author_id}))

    @staticmethod
    def save_message(self, message, author_id):
        room = Room.objects.get(id=self.room_id)
        author = User.objects.get(id=author_id)
        Message.objects.create(room=room, author=author, content=message)
