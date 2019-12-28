import asyncio
import aiohttp
from flags import BASE_URL, save_flag, show, main

"""
await表达式: 挂起coroutine的执行以等待一个awaitable对象
await表达式, async for 以及 async with 只能在协程函数体内部使用。
await表达式 用来获取协程运行的结果
await 相比 yield from 多了一个步骤, 验证它的 argument, await only accepts an awaitable:
    1) 原生协程对象.
    2) types.coroutine() 装饰的函数返回的 -> 协程生成器对象
    3) 一个具有 __await__ 方法的

每一个 yield from 链, 最后都是一个 yield 
"""


async def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    async with aiohttp.request('GET', url) as resp:
        image = await resp.read()
        return image


async def download_one(cc):
    image = await get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do)  # <coroutine object wait at 0x7fd3f93a8c40>
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()

    return len(res)


if __name__ == '__main__':
    main(download_many)
