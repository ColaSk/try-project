import asyncio
import socket

class SocketServer(object):

    def __init__(
        self, 
        host: str = '127.0.0.1', 
        port: int = 8000
    ):

        self.host = host
        self.port = port