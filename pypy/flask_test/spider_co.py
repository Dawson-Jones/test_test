import asyncio
import aiohttp
from aiohttp import web
import time


async def send_url(page_num):
    url = f'http://xidong.net/List000/Catalog_{page_num}_T1.html'
    async with aiohttp.ClientSession() as session:  # <8>
        # print('session', page_num)
        print('pend to send', page_num)
        async with session.get(url) as resp:
            if resp.status == 200:
                print('get:', page_num)
                # return await resp.read()
            else:
                print('not get:', page_num)
                raise web.HTTPNotFound()


def main():
    start = time.perf_counter()
    loop = asyncio.get_event_loop()
    url_li = [
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185,
        67, 97, 109, 117, 123, 127, 135, 141, 157, 169, 174, 66, 93, 5, 185
    ]
    tasks = [send_url(i) for i in url_li]
    futures = asyncio.wait(tasks)
    res, _ = loop.run_until_complete(futures)
    print(len(res))
    print('发送时间:', time.perf_counter() - start)
    # 330 用时 25
    # 960 45


if __name__ == '__main__':
    main()