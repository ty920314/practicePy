import multiprocessing


def down_data(q):
    """下载数据模拟"""
    data = [1, 2, 3]
    # 向队列中写入数据
    for tmp in data:
        q.put(tmp)
    print('下载完成')


def handle_data(q):
    """数据处理"""
    waiting = list()
    while True:
        data = q.get()
        waiting.append(data)

        if q.empty():
            break
    print(waiting)


def main():
    # 1创建一个队列
    q = multiprocessing.Queue(3)
    # 2创建多个进程，将队列的引用当做实参传递
    p1 = multiprocessing.Process(target=down_data, args=(q,))
    p2 = multiprocessing.Process(target=handle_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
