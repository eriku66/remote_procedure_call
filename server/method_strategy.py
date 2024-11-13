from abc import ABC, abstractmethod
from math import floor
from typing import List, Union


class MethodStrategy(ABC):
    @abstractmethod
    def process(self, params: List[Union[int, str]]):
        pass


class FloorMethod(MethodStrategy):
    def process(self, params: List[Union[int, str]]):
        if len(params) != 1:
            raise ValueError("Floor method expects exactly 1 parameter")

        try:
            x = float(params[0])
        except ValueError:
            raise ValueError("Floor method expects an float parameter")

        return floor(x)


class NRootMethod(MethodStrategy):
    def process(self, params: List[Union[int, str]]):
        if len(params) != 2:
            raise ValueError("NRoot method expects exactly 2 parameters")

        try:
            n, x = int(params[0]), int(params[1])
        except ValueError:
            raise ValueError("NRoot method expects integer parameters")

        return x ** (1 / n)


class ReverseMethod(MethodStrategy):
    def process(self, params: List[Union[int, str]]):
        if len(params) != 1:
            raise ValueError("Reverse method expects exactly 1 parameter")

        x = params[0]

        return x[::-1]


class ValidAnagramMethod(MethodStrategy):
    def process(self, params: List[Union[int, str]]):
        if len(params) != 2:
            raise ValueError("ValidAnagram method expects exactly 2 parameters")

        s, t = params

        return sorted(s) == sorted(t)


class SortMethod(MethodStrategy):
    def process(self, params: List[Union[int, str]]):
        return sorted(params)
