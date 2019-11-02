import asyncio


# 定义了一个简单的协程
async def simple_async():
    print('hello')
    await asyncio.sleep(1)  # 休眠1秒
    print('python')


def test_do_something():
    # 生成器产生多个协程对象
    task = [simple_async() for i in range(5)]

    # 获取一个事件循环对象
    loop = asyncio.get_event_loop()
    # 在事件循环中执行task列表
    loop.run_until_complete(asyncio.wait(task))


# 使用asynio中run方法运行一个协程
# asyncio.run(simple_async())
# 执行结果为
# hello
# python

test_do_something()
