#!/usr/bin/env python3
"""
11. More involved type annotations
"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    type annotations to the function
    Hint: look into TypeVar
    """
    if key in dct:
        return dct[key]
    else:
        return default
