from django.urls import re_path

from chat_app import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat_app/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer),
]