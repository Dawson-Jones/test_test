def consumer():
    r = ''
    while True:
        n = yield r  # 返回的是r, 通过send函数接收的是n, 通过next和send都可以唤醒执行
        # if not n:
        #     return
        print('[CONSUMER] consuming %s' % n)
        r = '200 OK'


def produce(c):
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCE] producing %s' % n)
        r = c.send(n)
        print('[PRODUCE] consumer return %s' % r)
    c.close()


if __name__ == '__main__':
    c = consumer()
    next(c)  # 必须使用None启动生成器 TypeError: can't send non-None value to a just-started generator
    produce(c)
