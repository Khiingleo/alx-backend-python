#!/usr/bin/env python3
"""A type annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """a type annotted function that takes a list of floats and returns
        a float of their sum.
    """
    return sum(input_list)
    # or
    # sum = 0.0
    # for num in input_list:
    #   sum += num
    # return num
