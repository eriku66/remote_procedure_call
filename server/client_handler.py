import socket

from request_handler import RequestHandler


class ClientHandler:
    def handle_client(self, client_socket: socket.socket):
        request_handler = RequestHandler()

        while True:
            request = request_handler.handle_request(client_socket)

            print(request)

            request_handler.send_response(client_socket, request)
