#!/usr/bin/env python3
"""defines a asynchronous function wait_n"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    function that takes in the wait_random from 0-basic_async_syntax
    and has spawns wait_random the number of times given and
    with the specified delay time
    Args:
        n(int): the number of times to spawn wait_random
        max_delay(int): the specified delay time
    Returns:
        (list[float]): a list of all the delays in ascending order
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delay = []

    for task in asyncio.as_completed(tasks):
        delay.append(await task)

    return delay
