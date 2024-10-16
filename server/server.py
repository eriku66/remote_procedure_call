import json
import threading

from client_handler import ClientHandler
from socket_server import SocketServer


def main():
    config = json.load(open("../config.json"))

    server_port = config["server_port"]

    socket_server = SocketServer(port=server_port)
    socket_server.bind()

    client_handler = ClientHandler()

    while True:
        client_socket = socket_server.accept()

        threading.Thread(
            target=client_handler.handle_client, args=(client_socket,)
        ).start()


if __name__ == "__main__":
    main()
