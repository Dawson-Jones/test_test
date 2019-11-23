class Province(object):
    country = '中国'

    def __init__(self, Province):
        self.Province = Province
        self.gender = '男'

    def print(self):
        print(f'我是{self.country}{self.Province}的{self.gender}人')

    def fix(self):
        self.country = '英国'
        # self.__class__.country = '英国'
        print('修改成功')

    @classmethod
    def class_attr_print(cls):
        print(cls.country)


u = Province('山东')
u.print()
u.fix()
u.print()
u.class_attr_print()
