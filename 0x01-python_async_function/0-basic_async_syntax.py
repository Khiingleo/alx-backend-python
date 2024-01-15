#!/usr/bin/env python3
"""Python asynchronous io function"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that takes in an int argument
    and waits for a random delay between 0 and max_delay
    and eventually returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
