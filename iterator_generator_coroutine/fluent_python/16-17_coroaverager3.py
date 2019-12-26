"""开始使用yield from"""

from collections import namedtuple
from coroutil import coroutine

Result = namedtuple('Result', 'count average')


# 子生成器
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


# 委派生成器
# @coroutine
def grouper(results, key):
    """ Q: 子生成器抛出StopIteration异常, 会让委派生成器恢复运行, 并把value值返回给委派生成器, 那么最终value值到底给了哪一个委派生成器呢???
        A: 跟子生成器最近的那个 yield from 委派生成器, 因为恢复运行后, yield from 处理了这个异常, 并拿到了返回值
        每一个yield from 在结束的时候都会触发StopIteration异常, 所以用死循环不让他停止, 而yield from会处理StopIteration异常
        所以, 在不加while True的情况下, 调用方需要对StopIteration进行处理, 也就是做的try except
    """
    while True:
        results[key] = yield from averager()
        print("grouper: ", results)


# 调用方
def main(data: dict):
    results = dict()
    for key, values in data.items():
        group = grouper(results, key)
        next(group)

        for value in values:
            group.send(value)

        # try:
        group.send(None)  # -> 如果使用except 捕获异常, 可以在grouper不使用 whlie
        # except StopIteration:
        #     pass

        """
        不需要这一句, 是因为, 外层for循环重新迭代的时候, 新建grouper实例, 绑定到了原来的group变量上, 
        前一个grouper实例(以及它创建的尚未终止的averager子生成器实例)被垃圾回收
        """
        # group.close()

    report(results)


# 输出报告
def report(results: dict):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


data = {
    'girls;kg': [40.9, 38.5, 44.3],
    'girls;m': [1.6, 1.51, 1.4],
    'boys;kg': [39.0, 40.8, 43.2],
    'boys;m': [1.38, 1.5, 1.32],
}

if __name__ == "__main__":
    main(data)
