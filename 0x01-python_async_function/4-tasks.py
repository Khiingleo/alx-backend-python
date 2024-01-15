#!/usr/bin/env python3
"""defines a asynchronous function wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    this function is nearly identical to 'wait_n' from
    '1-concurrent_coroutines' except 'task_wait_random' from
    '3-tasks' is being called instead of 'wait_random from
    '0-basic_async_syntax'
    Args:
        n(int): the number of times to spawn wait_random
        max_delay(int): the specified delay time
    Returns:
        (list[float]): a list of all the delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delay = []

    for task in asyncio.as_completed(tasks):
        delay.append(await task)

    return delay
