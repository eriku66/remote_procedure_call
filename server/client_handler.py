import json
import socket

from request_handler import RequestHandler
from request_processor import RequestProcessor
from response_handler import ResponseHandler


class ClientHandler:
    def __init__(
        self,
        request_handler: RequestHandler,
        response_handler: ResponseHandler,
        request_processor: RequestProcessor,
    ) -> None:
        self.request_handler = request_handler
        self.response_handler = response_handler
        self.request_processor = request_processor

    def handle_client(self, client_socket: socket.socket):
        while True:
            try:
                payload = self.request_handler.handle_request(client_socket)
                result = self.request_processor.process(payload)

                print(f"Result: {result}")

                self.response_handler.send_response(
                    client_socket, json.dumps({"result": result})
                )
                break
            except ValueError as e:
                print(f"Error: {e}")
                self.response_handler.send_response(
                    client_socket, json.dumps({"error": str(e)})
                )
                client_socket.close()
                break
            except Exception as e:
                print(f"Error: {e}")
                self.response_handler.send_response(
                    client_socket, "Internal server error"
                )
                client_socket.close()
                break
