class A(object):
    li = list()
    var = None

    def __init__(self, name):
        self.li.append(name)
        self.var = "var"


a = A("jdq")
print(A.li)  # ['jdq']
print(a.li)  # ['jdq']
print(a.li is A.li)  # True
b = A("dobby")
print(b.li)  # ['jdq', 'dobby']

print(A.var)  # None
print(a.var)  # var

"""
总结: 
如果是定义变量, 那么self会在自己的实例属性中新增一个同名的变量, 而不会去操作类属性中的那个同名变量
如果是操作已经定义好的变量, 那么self一层层的向上寻找是否有这个变量
"""
