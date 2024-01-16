#!/usr/bin/env python3
"""defines a coroutine measure_comprehension"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Import async_generator from the previous task and then
    write a coroutine called async_comprehension that takes
    no arguments.
    The coroutine will collect 10 random numbers using
    an async comprehensing over async_generator,
    then return the 10 random numbers.
    """
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end_time = time.perf_counter()

    return end_time - start_time
