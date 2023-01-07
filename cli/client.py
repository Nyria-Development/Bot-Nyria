import socket
import json


class CliClient(socket.socket):
    def __init__(self):
        super().__init__(family=socket.AF_INET, type=socket.SOCK_STREAM)
        with open("config.json", "r") as c:
            self.__config = json.load(c)
            self.__host = self.__config["cli"]["host"]
            self.__port = self.__config["cli"]["port"]


