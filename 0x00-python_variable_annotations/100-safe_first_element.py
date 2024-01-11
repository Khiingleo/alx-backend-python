#!/usr/bin/env python3
"""A duck-typed annotated function"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of the sequence or None if the
    sequence is empty"""
    if lst:
        return lst[0]
    else:
        return None
