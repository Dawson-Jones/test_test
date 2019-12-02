import threading
from time import sleep

"""
threading.Event: 'wait' for the same Event run 'set' function
threading.Thread: 'join' will blocking till the thread operation ending
"""


def test(n, event):
    print('Thread %s is ready' % n)
    event.wait()
    print('Thread %s is running' % n)


def main():
    event1 = threading.Event()
    event2 = threading.Event()
    # for i in range(2):
    #     th = threading.Thread(target=test, args=(i, event))
    #     th.start()
    th1 = threading.Thread(target=test, args=(1, event1))
    th2 = threading.Thread(target=test, args=(2, event2))
    th1.start()
    # th1.join()  # 死锁
    th2.start()
    print('----- event is set -----')
    event1.set()
    sleep(3)
    print('----- event is clear -----')
    event1.clear()


if __name__ == '__main__':
    main()
