import json
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import WebsocketConsumer
from inbox.models import Group, Message
from datetime import datetime

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()
        
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        print("NOO")

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json['message']
        group_id = text_data_json['group_id']
        user = self.scope['user']
        created_at=self.save_message(user, group_id, message)
        print(user)
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        user_ids = self.get_users(group_id)
        print(user_ids)
        for user_id in user_ids:
            room_group_name = 'chat_%d' % user_id
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'created_at': created_at,
                    'user_id': user.id
                }
            )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        user_id = event['user_id']
        created_at=event['created_at']
        created_at = datetime.strftime(created_at,'%H:%M')
        my_dictionary={
            'message': message,
            'created_at': created_at,
            'user_id': user_id,
        }
        # Send message to WebSocket
        self.send(text_data=json.dumps(my_dictionary))

    # @database_sync_to_async
    def get_users(self, group_id):
        group = Group.objects.get(pk=group_id)
        return group.users.values_list('id', flat=True)

    def save_message(self, user, group_id, message):
        group = Group.objects.get(pk=group_id)
        message=Message.objects.create(sender=user, group=group, text=message)
        # print(message.text)
        # print(message.sender)
        # print(message.created_at)


        return message.created_at
        