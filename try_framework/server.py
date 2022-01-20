import socketio
import logging
import uvicorn
from typing import Any

logger = logging.getLogger(__name__)

class AsyncSocketIOServer(object):

    def __init__(self):

        self.sio = socketio.AsyncServer(async_mode='asgi')
        self.app = socketio.ASGIApp(self.sio)

    def register_namespace(self, namespace_handler):
        self.sio.register_namespace(namespace_handler)

    def run(self, **kwargs: Any):
        uvicorn.run(self.app, **kwargs)

    