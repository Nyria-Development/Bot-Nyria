import socket
import json


class CliServer(socket.socket):
    def __init__(self):
        super().__init__(family=socket.AF_INET, type=socket.SOCK_STREAM)

        with open("config.json", "r") as c:
            self.__config = json.load(c)
            self.__host = self.__config["cli"]["host"]
            self.__port = self.__config["cli"]["port"]

            self.bind((self.__host, self.__port))
            self.listen(5)
            print("Waiting")

    async def waiting(self):
        while True:
            # Establish connection with client.
            c, addr = self.accept()
            print('Got connection from', addr)
            c.send('Thank you for connecting'.encode())
            c.close()
            break
