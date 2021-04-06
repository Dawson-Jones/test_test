from concurrent import futures
from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []  # every object in list is future
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)  # submit() 排定可调用对象的执行时间, 然后返回一个 future 表示这个待执行的操作
            to_do.append(future)
            msg = 'Scheduled  for {}: {}'
            print(msg.format(cc, future))
            # Scheduled  for CN: <Future at 0x7ff07a6ec6d0 state=running>

        results = []
        for future in futures.as_completed(to_do):  # yield future when future finished
            # when call "result()" on future finished will return "result of callable object" -> result of download_one
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            # CN <Future at 0x7ff07a6ec6d0 state=finished returned str> result: 'CN'
            results.append(res)

    return len(results)


if __name__ == "__main__":
    main(download_many)
