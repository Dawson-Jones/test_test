import types


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