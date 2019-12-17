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
@coroutine
def grouper(results, key):
    while True:
        results[key] = yield from averager()

# 调用方 
def main(data: dict):
    results = dict()
    for key, values in data.items():
        group = grouper(results, key)

        for value in values:
            group.send(value)
        group.send(None)

    # print(results)
    report(results)

# 输出报告
def report(results: dict):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))

data = {
    'girls;kg': [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m': [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, .133, 1.46, 1.45, 1.43],
    'boys;kg': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == "__main__":
    main(data)
    """
    10 girls averaging 42.04kg
    10 girls averaging 42.04kg
    10 girls averaging 1.31m
     9 boys  averaging 40.42kg
    10 girls averaging 42.04kg
    10 girls averaging 1.31m
     9 boys  averaging 40.42kg
     9 boys  averaging 1.39m
    10 girls averaging 42.04kg
    10 girls averaging 1.31m
    """ 