# Coroutines, tasks, futures

import asyncio
import time


async def coroutine_func_1():
    await asyncio.sleep(1)
    print('coroutine_func_1')


async def coroutine_func_2():
    await asyncio.sleep(2)
    print('coroutine_func_2')


async def main():
    print(time.strftime('%X'))
    await coroutine_func_1()
    await coroutine_func_2()
    print(time.strftime('%X'))

    print(time.strftime('%X'))
    task1 = asyncio.create_task(coroutine_func_1())
    task2 = asyncio.create_task(coroutine_func_2())

    await task1
    await task2
    print(time.strftime('%X'))

asyncio.run(main())





