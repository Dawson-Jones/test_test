import asyncio
import threading

"""
@asyncio.coroutine to async
yield from to await

the result is actually same
"""


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


# async def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     await asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())


# 获取EventLoop:
loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

