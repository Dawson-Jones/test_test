from coroutil import coroutine


class DemoException(Exception):
    """demo异常"""


@coroutine
def demo_exc_handling():
    print("-> coroutine started")
    while True:
        try:
            x = yield
        except DemoException:
            print("*** DemoExcepition handled. continuing...")
        else:
            print("-> coroutine received: {!r}".format(x))


if __name__ == "__main__":
    exc_coro = demo_exc_handling()
    exc_coro.send(11)
    exc_coro.throw(DemoException)
