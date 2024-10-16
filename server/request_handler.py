import socket


class RequestHandler:
    def handle_request(self, client_socket: socket.socket):
        request = client_socket.recv(1024)

        return request.decode()

    def send_response(self, client_socket: socket.socket, response: str) -> None:
        client_socket.sendall(response.encode())
