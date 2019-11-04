import time


class Sample1:
    A = 'Foo'

    def __enter__(self):
        print("in __enter__")
        # return "Foo"  # 返回值作为as后面的东西
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("in __exit__")

    def show(self):
        return self.A


def get_sample():
    return Sample1()


with get_sample() as sample:
    time.sleep(3)
    # print("Sample: ", sample)
    print("Sample: ", sample.show())


# ================================


# class Sample2(object):
#     def __enter__(self):
#         print('in enter')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("type: ", exc_type)
#         print("val: ", exc_val)
#         print("tb: ", exc_tb)
#
#     @staticmethod
#     def do_something():
#         bar = 1 / 0
#         return bar + 10
#
#
# with Sample2() as sample:
#     sample.do_something()
