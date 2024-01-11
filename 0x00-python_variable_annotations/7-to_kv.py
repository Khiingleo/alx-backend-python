#!/usr/bin/env python3
"""a type annotated function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A type annotated function that returns the k and the
    square of the v as a tuple"""
    return (k, v**2)
