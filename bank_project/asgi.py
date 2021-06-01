import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import notifier.routing
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bank_project.settings")

application = ProtocolTypeRouter({
    # value of the http - returning value of the asgi app function
    "http": get_asgi_application(),
    # value of the ws -  returning value of the AuthMiddlewareStack
    "websocket": AuthMiddlewareStack(
        # arguments as URLRouter
        URLRouter(
            notifier.routing.websocket_urlpatterns
        )
    ),
})
