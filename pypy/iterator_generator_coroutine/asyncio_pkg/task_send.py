import json
import aiohttp
import asyncio
import requests

from aiohttp import web

# HOST = "127.0.0.1:8080"
HOST = "39.106.50.219:8080"
# HOST = "47.99.151.242:8080"


async def send_http(body: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"http://{HOST}/api/v1/patch/add", data=body.encode()) as resp:
            if resp.status == 200:
                print("------")
            else:
                raise web.HTTPNotFound()


def async_send():
    with open("task_sche.json") as f:
        obj = json.load(f)

    import time

    bodys = []
    tasks = []
    for task in obj["RECORDS"]:
        body = json.dumps(
            {
                "token": "sBtwBL5aqu8WNgUhgCv9doPqT",
                "data": [{"task_id": task["task_id"], "circle": int(task['circle'])}],
                "call_back_url": "http://127.0.0.1:8090/monitor_event"
            }
        )

        bodys.append(body)

    loop = asyncio.get_event_loop()
    st = time.time()
    for body in bodys:
        co = send_http(body)
        tasks.append(co)

    futures = asyncio.wait(tasks)
    res, _ = loop.run_until_complete(futures)
    print(len(res))
    print(time.time() - st)

def common_send():
    with open("task_sche.json") as f:
        obj = json.load(f)

    for task in obj["RECORDS"]:
        body = {
            "token": "sBtwBL5aqu8WNgUhgCv9doPqT",
            "data": [{"task_id": task["task_id"], "circle": int(task['circle'])}],
            "call_back_url": "http://127.0.0.1:8090/monitor_event"
        }

        print(requests.post(f"http://{HOST}/api/v1/patch/add", json=body).status_code)

    # body = {
    #     "token": "sBtwBL5aqu8WNgUhgCv9doPqT",
    #     "data": [{"task_id": "895c18db32cb367de2c81bf86c0375bc", "circle": 30}],
    #     "call_back_url": "http://47.97.197.19:8080/monitor_event?flag=c5f2dacce5bd9c0a41ca578fb644dcd2"
    # }
    # print(requests.post(f"http://{HOST}/api/v1/patch/add", json=body).status_code)


if __name__ == '__main__':
    # common_send()
    async_send()
