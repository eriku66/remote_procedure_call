from method import Method
from request_payload import RequestPayload


class RequestProcessor:
    def process(self, payload: RequestPayload):
        try:
            method = Method(payload.method)
        except Exception:
            raise ValueError(f"Unknown method: {payload.method}")

        return method.process(payload.params)


_request_processor = None


def get_request_processor() -> RequestProcessor:
    global _request_processor

    if _request_processor is None:
        _request_processor = RequestProcessor()

    return _request_processor
