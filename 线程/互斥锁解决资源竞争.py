# 定义一个全局变量
import threading
import time

g_num = 0


def test1():
    global g_num
    # 上锁 如果之前没有上锁 此时上锁成功 否则堵塞

    for i in range(1000000):
        mutex.acquire()
        g_num += 1
        mutex.release()
    # 解锁

    print("------test1 g_num=%d" % g_num)


def test2():
    global g_num
    for i in range(1000000):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("------test2 g_num=%d" % g_num)


# 创建互斥锁，默认没上锁
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    t2.start()

    time.sleep(3)


if __name__ == "__main__":
    main()
