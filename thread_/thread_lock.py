import threading
import time

g_num = 0


def test1(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()


def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()


mutex = threading.Lock()

if __name__ == '__main__':
    start = time.perf_counter()
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end = time.perf_counter()
    print(g_num, end-start)

