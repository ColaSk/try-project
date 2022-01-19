import socketio
import logging
import uvicorn
from typing import Any

logger = logging.getLogger(__name__)

class ServerNamespace(socketio.AsyncNamespace):

    async def on_connect(self, sid: Any , environ: Any):
        logger.info(f'sid: {sid} connect success')

    async def on_disconnect(self, sid: Any):
        logger.info(f'sid: {sid} disconnect success')
    
    async def on_handler(self, sid, data):
        logger.info(f'sid: {sid} my_response: {data}')

class AsyncSocketIOServer(object):

    def __init__(self):

        self.sio = socketio.AsyncServer(async_mode='asgi')
        self.sio.register_namespace(ServerNamespace('/sio-try'))
        self.app = socketio.ASGIApp(self.sio)

    def run(self, **kwargs: Any):
        uvicorn.run(self.app, **kwargs)

    