import asyncio


async def do_some_work(x):
    print('waiting: ', x)
    await asyncio.sleep(x)
    return f'Done after {x}s'


coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

# result
for task in tasks:
    print('Task ret: ', task.result())
