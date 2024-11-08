from dataclasses import dataclass
from typing import List, Union


@dataclass
class RequestPayload:
    method: str
    params: List[Union[int, str]]

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not isinstance(self.method, str):
            raise ValueError("Method must be a string")

        if not isinstance(self.params, list):
            raise ValueError("Params must be a list")
        if not all(isinstance(item, (int, str)) for item in self.params):
            raise ValueError("All items in params must be integers or strings")
