import socket


class Server:
    def __init__(self):
        self.__socket = socket.socket()

    def broadcast(self):
