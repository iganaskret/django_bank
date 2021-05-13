from django.urls import path

from .consumers import NotifierConsumer

websocket_urlpatterns = [
    path(r'ws/some_url/', NotifierConsumer.as_asgi()),
]
