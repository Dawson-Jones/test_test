def fib(n):
    print('进入')
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, num2 + num1
        current += 1
        yield num

    return 'done'


F = fib(10)  # 运行到这里没有任何反映
# print(next(F))
for i in F:
    print(i)

"""
yield:
1. 保存运行状态-断点, 暂停执行将生成器挂起
2. 将yield垢面表达式的值, 作为返回值返回 此时相当于return
"""

# 使用yield实现协程
import time


def work1():
    current = 0
    while True:
        yield f'work1 {current}th called'
        current += 1


def work2():
    current = 0
    while True:
        yield f'work2 {current}th called'
        current += 1


def main():
    w1 = work1()
    w2 = work2()
    while True:
        print(next(w1))
        print(next(w2))
        time.sleep(1)


if __name__ == '__main__':
    main()
