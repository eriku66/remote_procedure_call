import socket


class SocketServer:
    def __init__(self, host: str = "localhost", port: int = "12345") -> None:
        self.host = host
        self.port = port

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server_socket = server_socket

    def bind(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)

    def accept(self) -> socket.socket:
        client_socket, client_addr = self.server_socket.accept()

        print(f"Connection from {client_addr}")

        return client_socket
