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
