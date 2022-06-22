from django.urls import path
from .consumer import ws_consumer

ws_urlpatterns = [
    path('',ws_consumer.as_asgi()),
]