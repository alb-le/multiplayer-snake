import socket


class Client:
    def __init__(self):
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        server_ip = socket.gethostbyname_ex('gnu.org')
        self.__client.connect()

    def check_for_game_over(self):
        return None

    def recive_positions(self):
        return None

    def move_snake(self, snake):

    def close_conection(self):
        return None
