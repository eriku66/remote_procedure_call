from enum import Enum
from typing import List, Union

from method_strategy import (
    FloorMethod,
    NRootMethod,
    ReverseMethod,
    SortMethod,
    ValidAnagramMethod,
)


class Method(Enum):
    FLOOR = "floor"
    NROOT = "nroot"
    REVERSE = "reverse"
    VALID_ANAGRAM = "validAnagram"
    SORT = "sort"

    def process(self, params: List[Union[int, str]]) -> Union[int, str]:
        match self:
            case Method.FLOOR:
                return FloorMethod().process(params)
            case Method.NROOT:
                return NRootMethod().process(params)
            case Method.REVERSE:
                return ReverseMethod().process(params)
            case Method.VALID_ANAGRAM:
                return ValidAnagramMethod().process(params)
            case Method.SORT:
                return SortMethod().process(params)
