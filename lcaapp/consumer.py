import json
import re
from channels.generic.websocket import WebsocketConsumer
from .models import out
from django.core import serializers

class ws_consumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        while(True):
            res = out.objects.latest('id')
            serialized_obj = serializers.serialize('json',[res,])
            self.send(json.dumps({'output':serialized_obj}))