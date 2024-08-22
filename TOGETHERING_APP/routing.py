from django.urls import re_path

from .consumer import Chatting

websocket_urlpatterns = [
    re_path(r"wss/watch/(?P<room_name>\w+)/$", Chatting.as_asgi()),
]
