import json
import socket

from request_handler import RequestHandler
from response_handler import ResponseHandler


class ClientHandler:
    def __init__(
        self, request_handler: RequestHandler, response_handler: ResponseHandler
    ) -> None:
        self.request_handler = request_handler
        self.response_handler = response_handler

    def handle_client(self, client_socket: socket.socket):
        while True:
            try:
                payload = self.request_handler.handle_request(client_socket)
                result = self.process_request(payload)
                self.response_handler.send_response(
                    client_socket, json.dumps({"result": result})
                )
            except Exception as e:
                print(f"Error: {e}")
                client_socket.close()
                break

    def process_request(self, payload):
        return "Connection is successful"
