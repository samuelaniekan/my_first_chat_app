# chat/routing.py
from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
     re_path(r'ws/chat/(?P<uri>\w+)/$', consumers.ChatConsumer.as_asgi()),
]