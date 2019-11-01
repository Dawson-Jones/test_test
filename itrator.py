class MyList(object):
    def __init__(self):
        self.item = []
        self.current = 0

    def add(self, val):
        self.item.append(val)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.item):
            item = self.item[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration


if __name__ == '__main__':
    my_list = MyList()
    my_list.add(1)
    my_list.add(2)
    my_list.add(3)
    my_list.add(4)
    my_list.add(5)
    for num in my_list:
        print(num)

"""
使用for循环时
1. 判断对象是否可以迭代(是否有__iter__方法)
2. 1成立的前提下, 通过iter函数得到对象的__iter__方法的返回值  -> iter(对象)会自动调用对象的__iter__魔法方法
3. __iter__方法的返回值是一个迭代器
4. for循环通过迭代器的__next__函数取值
"""


# Eg
class FibIterator(object):
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.num1 = 0
        self.num2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.current += 1
            return num
        else:
            raise StopIteration


f = FibIterator(10)
for i in f:
    print(i, end='\n')
