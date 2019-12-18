from coroutil import coroutine


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


if __name__ == "__main__":
    """
    无装饰器
    coro_avg = averager()
    coro_avg.__next__()  # 预激协程, 使其运行到yield的右支
    for i in range(100):
        avg = coro_avg.send(i)
        print(avg)
    """
    coro_avg = averager()
    for i in range(100):
        avg = coro_avg.send(i)
        print(avg)

    print(Ellipsis)
