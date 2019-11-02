import os
import sys
import asyncio
import requests
import time

url = 'https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn={}'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}
project_path = os.path.split(sys.argv[0])[0]


async def main(page):
    per_url = url.format(page * 50)
    print('send http request')
    # await asyncio.sleep(1)
    # await parse_url(per_url, page)
    ret = await asyncio.create_task(parse_url(per_url, page))
    print('writing file', ret)


async def parse_url(per_url, page_num):
    response = requests.get(url=per_url, headers=headers)
    result = response.content.decode()

    file_name = f'lol-page{page_num}.html'
    target_path = os.path.join(project_path, 'lol')
    file_path = os.path.join(target_path, file_name)
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(result)
    return f'OK {page_num}'


def do_something():
    tasks = [main(i) for i in range(10)]
    # 获取一个事件循环对象
    loop = asyncio.get_event_loop()
    # 在事件循环中执行tasks列表
    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    start = time.perf_counter()
    # asyncio.run(main())
    do_something()
    end = time.perf_counter()
    print(f'用时: {end - start}')  # 15.6  14  后: 14.7
