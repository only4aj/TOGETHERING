from django.urls import re_path

from .consumer import Chating

websocket_urlpatterns = [
    re_path(r"ws/watch/(?P<room_name>\w+)/$", Chating.as_asgi()),
]
