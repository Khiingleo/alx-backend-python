#!/usr/bin/env python3
"""An asynchronous generator function"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    aynchronous generator function that takes in no argument and
    loops ten(10) times, each time it asynchronously waits 1 second
    and then yealds a random number between 0 and 10 using
    random.uniform()
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
