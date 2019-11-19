import types

"""
装饰器@asyncio.coroutine 相当于 async

有yield就是一个生成器
yield from 如果子生成器没有return, 这是一个生成器; 如果子生成器有return, 这是一个协程, 协程相当于await
yield from 包含 await. yield from是一个双向管道, yield是挂起自身并返回结果, yield from是挂起自身并返回后面跟的生成器或协程的结果
"""


def function():
    return 1


def generator():
    yield 1


# 异步函数
async def async_function():
    return 1


# await 挂起自身的协程, 并等待另一个协程完成直到返回结果
async def await_coroutine():
    result = await async_function()
    print(f'result is {result}')


# 异步生成器
async def async_generator():
    yield 1


# print(isinstance(function, types.FunctionType))
# print(isinstance(generator(), types.GeneratorType))
# print(isinstance(async_function(), types.CoroutineType))
# print(isinstance(async_generator(), types.AsyncGeneratorType))

# print(async_function().send(None))

def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        print(f'stop is {e.value}')


run(await_coroutine())
