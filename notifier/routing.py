from django.urls import path

from .consumers import NotifierConsumer

# list of url patterns
# url address ws, handler for all the requests to this url (cunsumer)
websocket_urlpatterns = [
    path(r'ws/notifier/', NotifierConsumer.as_asgi()),
]
