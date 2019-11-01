import asyncio


# 内部协程函数
async def do_some_work(x):
    print('waiting', x)
    await asyncio.sleep(x)
    return f'Done after {x}s'


# 外部协程函数
async def main():
    tasks = [
        do_some_work(1),
        do_some_work(2),
        do_some_work(4)
    ]

    # 【重点】：await 一个task列表（协程）
    # dones：表示已经完成的任务
    # pendings：表示未完成的任务
    dones, pendings = await asyncio.wait(tasks)

    for task in dones:
        print('Task ret: ', task.result())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
