import socket


class ResponseHandler:
    def send_response(self, client_socket: socket.socket, response: str) -> None:
        client_socket.sendall(response.encode())
        client_socket.close()


_response_handler = None


def get_response_handler():
    global _response_handler

    if _response_handler is None:
        _response_handler = ResponseHandler()

    return _response_handler
