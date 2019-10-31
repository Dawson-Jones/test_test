class A(object):
    def __init__(self):
        self.integer1 = 2
        self.float1 = 1.0

    def plus(self):
        print(self.integer1 + self.float1)

a = A()
a.integer1 = 3
a.float1 = 3
a.plus()

