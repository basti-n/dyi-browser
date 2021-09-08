from typing import Union
from core.constants.constants import Ports
from core.socket import create_socket
import socket
import ssl


class SocketService():

    def __init__(self, host: str) -> None:
        self.host = host
        self.ctx = ssl.create_default_context()
        self.secure = True

    def create(self, *, secure=True) -> Union[socket.socket, ssl.SSLSocket]:
        self.secure = secure
        self.socket = self.use_tls(
            create_socket()) if secure else create_socket()

        return self.socket

    def connect(self) -> None:
        if not self.socket:
            print('No Socket found. Please create socket first.')

        else:
            self.socket.connect(
                (self.host, (Ports.HTTPS if self.secure else Ports.HTTP).value))

    def use_tls(self, socket: socket.socket) -> ssl.SSLSocket:
        return self.ctx.wrap_socket(socket, server_hostname=self.host)
