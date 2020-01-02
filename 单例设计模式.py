class MusicPlayer(object):
    _instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        print('__new__方法')
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

    def __init__(self):
        if self.init_flag:
            return
        print("初始化中...")
        self.init_flag = True


"""
    1. self.属性 并不能改变 类属性的值
    2. 但是在这个地方 第二个实例确实判定了 self.init_flag为 True
    3. __new__ 方法会返回一个实例对象, 也就是说__new__方法执行完, 实例化完成
    4. 每次实例化一个对象, 总会执行 __new__ 和 __init__ 方法, __new__ 方法返回的是这个实例对象, __init__ 负责设定一些初始值
"""
player1 = MusicPlayer()
player2 = MusicPlayer()

print(player1)
print(MusicPlayer.init_flag)
print(player2)

if player1 is player2:
    print('yes')
