import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

ctime = -1

class Chatting(WebsocketConsumer):
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
                global ctime
                if ctime != int(current_time):
                    ctime = int(current_time)
                    async_to_sync(self.channel_layer.group_send)(
                        self.room_name, {
                            'type': 'video_play',
                            'current_time': current_time
                        }
                    )
            elif message_type == 'video.pause':
                current_time = data['current_time']
                async_to_sync(self.channel_layer.group_send)(
                    self.room_name, {
                        'type': 'video_pause',
                        'current_time': current_time
                    }
                )
            elif message_type == 'audio.stream':
                # Handle the audio streaming data
                async_to_sync(self.channel_layer.group_send)(
                    self.room_name, {
                        'type': 'audio_stream',
                        'audio_data': data['audio_data']
                    }
                )
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
        self.send(text_data=json.dumps({
            'message_type': 'video.play',
            'current_time': current_time
        }))

    def video_pause(self, event):
        current_time = event['current_time']
        self.send(text_data=json.dumps({
            'message_type': 'video.pause',
            'current_time': current_time
        }))

    def audio_stream(self, event):
        audio_data = event['audio_data']
        self.send(text_data=json.dumps({
            'message_type': 'audio.stream',
            'audio_data': audio_data
        }))
