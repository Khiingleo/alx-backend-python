#!/usr/bin/env python3
"""defines A function that makes use of async comprehension"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects 10(ten) random numbers using an async comprehension
    over aync_generator, then return the 10 random numbers
    """
    result = [number async for number in async_generator()]
    return result
