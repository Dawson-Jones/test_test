from coroutil import coroutine
from collections import namedtuple

Result = namedtuple("Result", "count average")


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is Ellipsis:
            break
        total += term
        count += 1
        average = total / count
    
    return Result(count, average)


if __name__ == "__main__":
    coro_avg = averager()
    coro_avg.send(10)
    coro_avg.send(30)
    coro_avg.send(6.5)
    try:
        coro_avg.send(Ellipsis)
    except StopIteration as exc:
        result = exc.value
        print(result)
