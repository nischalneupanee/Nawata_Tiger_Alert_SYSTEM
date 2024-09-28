from django.urls import path,re_path

#
# websocket_urlpatterns = [
#     path(r'ws/webcam/', consumers.WebcamConsumer.as_asgi()),
# ]

from django.urls import path
from .consumers import WebcamConsumer,VideoDemoConsumer

websocket_urlpatterns = [
    path('ws/videostream/', VideoDemoConsumer.as_asgi()),
    path('ws/webcam/', WebcamConsumer.as_asgi()),
]
