import os
import sys
import requests
import time


class TiebaSpider(object):
    def __init__(self, name):
        self.name = name
        self.url = "https://tieba.baidu.com/f?kw=" + name + "&ie=utf-8&pn={}"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
        }
        self.project_path = os.path.split(sys.argv[0])[0]

    def save_html(self, response, page_num):
        file_path = f'{self.name}吧-第{page_num}页.html'
        target_path = os.path.join(self.project_path, self.name)
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        with open(f'{target_path}/{file_path}', 'w', encoding='utf-8') as f:
            f.write(response)

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def run(self):
        url_list = [self.url.format(i * 50) for i in range(10)]
        for url in url_list:
            response = self.parse_url(url)
            page_num = url_list.index(url) + 1
            self.save_html(response, page_num)


if __name__ == "__main__":
    start = time.perf_counter()
    liyi = TiebaSpider('lol')
    liyi.run()
    end = time.perf_counter()
    print(f'用时: {end - start}')  # 用时14.2
