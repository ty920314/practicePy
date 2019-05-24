import os
import random
import time
from multiprocessing.pool import Pool


def worker(msg):
    t_start = time.time()
    print("%s 开始执行，进程号为%d" % (msg, os.getpid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完成，耗时%0.2f" % (t_stop - t_start))


po = Pool(3)


def main():
    for i in range(10):
        po.apply_async(worker, (i,))
    print('start-------')
    po.close()
    po.join()
    print('end---------')


if __name__ == "__main__":
    main()
