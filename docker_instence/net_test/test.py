import time
import requests


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    url = "https://www.bilibili.com"
    # url = "http://host.docker.internal:64150"       # 与本机通信
    try:
        resp = requests.get(url, headers=headers)
    except Exception as e:
        print("some wrong happend", e)
    else:
        # with open("./test", "a") as f:
        #     f.write(str(resp.status_code))
        print(resp.headers)


if __name__ == '__main__':
    # while True:
    main()
    time.sleep(2)
