import json
import socket

from request_payload import RequestPayload


class RequestHandler:
    def handle_request(self, client_socket: socket.socket) -> RequestPayload:
        request = client_socket.recv(4096)

        try:
            return RequestPayload(**json.loads(request.decode()))
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f"Invalid JSON at position {e.pos}", request.decode(), e.pos
            )
        except ValueError as e:
            raise e


_request_handler = None


def get_request_handler() -> RequestHandler:
    global _request_handler

    if _request_handler is None:
        _request_handler = RequestHandler()

    return _request_handler
