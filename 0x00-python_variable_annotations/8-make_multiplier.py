#!/usr/bin/env python3
"""A type annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by a given multiplier"""

    def multiplier_function(x: float) -> float:
        """performs the multiplication"""
        return x * multiplier
    return multiplier_function
