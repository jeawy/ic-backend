import json

from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Chat
from user.models import User


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        user1 = self.scope['user'].username
        user2 = self.room_name
        self.group_name = f"chat_{''.join(sorted([user1, user2]))}"

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = self.scope['user']
        reciever = await self.get_reciever_user()

        await self.save_message(sender, reciever, message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.username,
                'reciever': reciever.username
            }
        )
        print(self.room_group_name, "----------------------")

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        receiver = event['receiver']

        await self.send(text_data=json.dumps({
            'sender': sender,
            'reciever': receiver,
            'message': message,
        }))

    @sync_to_async
    def get_reciever_user(self):
        return User.objects.get(username=self.room_name)

    @sync_to_async
    def save_message(self, sender, reciever, message):
        Chat.objects.create(sender=sender, reciever=reciever, message=message)
