"""middleware attributes configuration"""
from django.apps import AppConfig


class MiddlewareConfig(AppConfig):
    """middleware configuration applies to"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'middleware'
