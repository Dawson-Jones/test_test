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


async def main():
    complete_urls = [url.format(i * 50) for i in range(10)]
    for per_url in complete_urls:
        print('发送http请求')
        result = await parse_url(per_url)
        page_num = complete_urls.index(per_url)
        print('写文件')
        await save_html(result, page_num)


async def parse_url(per_url):
    response = requests.get(url=per_url, headers=headers)
    return response.content.decode()


async def save_html(result, page_num):
    file_name = f'lol-page{page_num}.html'
    target_path = os.path.join(project_path, 'lol')
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    file_path = os.path.join(target_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(result)


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f'用时: {end - start}')  # 15.6  14
