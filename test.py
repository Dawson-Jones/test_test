import asyncio
import time


async def hello(name):
    print('Hello,', name)


# 定义协程对象
coroutine = hello("World")
# 定义事件循环对象容器
loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# 将协程转为task任务
task = loop.create_task(coroutine)
# 将task任务扔进事件循环对象中并触发
loop.run_until_complete(task)


# ===============================


async def _sleep(x):
    time.sleep(2)
    return '暂停了{}秒！'.format(x)


coroutine = _sleep(2)
loop = asyncio.get_event_loop()

task = asyncio.ensure_future(coroutine)
loop.run_until_complete(task)

# task.result() 可以取得返回结果
print('返回结果：{}'.format(task.result()))


# ====================================
async def _sleep(x):
    time.sleep(2)
    return '暂停了{}秒！'.format(x)


def callback(future):
    print('这里是回调函数，获取返回结果是：', future.result())


coroutine = _sleep(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)

# 添加回调函数
task.add_done_callback(callback)

loop.run_until_complete(task)
