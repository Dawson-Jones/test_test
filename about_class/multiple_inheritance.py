class Parent(object):
    def __init__(self, name, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        self.name = name
        print('parent的init结束被调用, 名字: ', self.name)


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        self.age = age
        super().__init__(name, *args, **kwargs)  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son1的init结束被调用, 年龄: ', self.age)


class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        self.gender = gender
        super().__init__(name, *args, **kwargs)  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son2的init结束被调用, 性别: ', self.gender)


class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        # 多继承时，相对于使用类名.__init__方法，要把每个父类全部写一遍
        # 而super只用一句话，执行了全部父类的方法，这也是为何多继承需要全部传参的一个原因
        # super(Grandson, self).__init__(name, age, gender)
        super().__init__(name, age, gender)
        print('Grandson的init结束被调用')


gs = Grandson('grandson', 12, '男')
print(Grandson.__mro__)
