import json
# import time
import asyncio
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


ctime = -1

class Chating(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        async_to_sync(self.channel_layer.group_add)(
            self.room_name, self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name, self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        if 'message_type' in data:
            message_type = data['message_type']
            if message_type == 'video.play':
                current_time = data['current_time']
                # Broadcast play event with current time to all clients
                print(current_time)
                # time.sleep(10)
                # asyncio.sleep(2)
                global ctime
                if ctime!=int(current_time):
                    ctime = int(current_time)
                    async_to_sync(self.channel_layer.group_send)(
                        self.room_name, {
                            'type': 'video_play',
                            'current_time': current_time
                        }
                    )
            elif message_type == 'video.pause':
                current_time = data['current_time']
                # Broadcast pause event with current time to all clients
                async_to_sync(self.channel_layer.group_send)(
                    self.room_name, {
                        'type': 'video_pause',
                        'current_time': current_time
                    }
                )
            # Handle other message types if needed
        else:
            msg = data["message"]
            async_to_sync(self.channel_layer.group_send)(
                self.room_name, {
                    'type': 'chat_messages',
                    'messages': msg,
                    'user': str(self.scope['user'])
                }
            )

    def chat_messages(self, event):
        msg = event["messages"]
        self.send(text_data=json.dumps({
            "message": msg,
            "user": event["user"]
        }))

    def video_play(self, event):
        current_time = event['current_time']
        # Update video playback time on client-side
        self.send(text_data=json.dumps({
            'message_type': 'video.play',
            'current_time': current_time
        }))

    def video_pause(self, event):
        current_time = event['current_time']
        # Update video playback time on client-side
        self.send(text_data=json.dumps({
            'message_type': 'video.pause',
            'current_time': current_time
        }))





# import json
# from channels.generic.websocket import WebsocketConsumer
# from asgiref.sync import async_to_sync

# class Chating(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_name, self.channel_name
#         )
#         self.accept()

#     def disconnect(self, code):
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_name, self.channel_name
#         )

#     def receive(self, text_data=None, bytes_data=None):
#         data = json.loads(text_data)
        
#         if 'message_type' in data:
#             message_type = data['message_type']
#             if message_type == 'video.play':
#                 current_time = data['current_time']
#                 video_id = data['video_id']
#                 async_to_sync(self.channel_layer.group_send)(
#                     self.room_name, {
#                         'type': 'video.play',
#                         'current_time': current_time,
#                         'video_id': video_id
#                     }
#                 )
#             elif message_type == 'video.pause':
#                 current_time = data['current_time']
#                 async_to_sync(self.channel_layer.group_send)(
#                     self.room_name, {
#                         'type': 'video.pause',
#                         'current_time': current_time
#                     }
#                 )
#             elif message_type == 'video.sync':
#                 video_id = data['video_id']
#                 current_time = data['current_time']
#                 async_to_sync(self.channel_layer.group_send)(
#                     self.room_name, {
#                         'type': 'video.sync',
#                         'current_time': current_time,
#                         'video_id': video_id
#                     }
#                 )
#         else:
#             msg = data["message"]
#             async_to_sync(self.channel_layer.group_send)(
#                 self.room_name, {
#                     'type': 'chat_messages',
#                     'messages': msg,
#                     'user': str(self.scope['user'])
#                 }
#             )

#     def chat_messages(self, event):
#         msg = event["messages"]
#         self.send(text_data=json.dumps({
#             "message": msg,
#             "user": event["user"]
#         }))

#     def video_play(self, event):
#         current_time = event['current_time']
#         video_id = event['video_id']
#         self.send(text_data=json.dumps({
#             'message_type': 'video.play',
#             'current_time': current_time,
#             'video_id': video_id
#         }))

#     def video_pause(self, event):
#         current_time = event['current_time']
#         self.send(text_data=json.dumps({
#             'message_type': 'video.pause',
#             'current_time': current_time
#         }))

#     def video_sync(self, event):
#         current_time = event['current_time']
#         video_id = event['video_id']
#         self.send(text_data=json.dumps({
#             'message_type': 'video.sync',
#             'current_time': current_time,
#             'video_id': video_id
#         }))
