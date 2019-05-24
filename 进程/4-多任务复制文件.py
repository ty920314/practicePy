import multiprocessing
import os
from multiprocessing import Manager


def copy_file(q, file_name, old_folder_name, new_folder_name):
    f = open(old_folder_name + '/' + file_name, 'rb')
    content = f.read()
    f.close()
    new_f = open(new_folder_name + '/' + file_name, 'wb')
    new_f.write(content)
    new_f.close()

    #拷贝完向队列中put一个消息
    q.put(file_name)

def main():
    # 1获取要copy的文件夹名字
    old_folder_name = input('请输入要copy的文件夹名字：')

    # 2创建一个新文件夹
    new_folder_name = old_folder_name + '复件'
    os.mkdir(new_folder_name)
    # 3打开文件写数据 listdir()
    file_names = os.listdir(old_folder_name)

    # 4创建进程池子

    # 5复制原文件夹中的文件到新文件
    po = multiprocessing.Pool(2)

    q = Manager().Queue()
    # 向进程池中添加copy的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))
    po.close()
    # po.join()
    # 进度条 queue实现
    all_file_num = len(file_names)
    copy_num = 0
    while True:
        # file_name = q.get()
        # print('已完成copy:%s' % file_name)
        print('拷贝的进度 %.2f %%' % (copy_num*100/all_file_num))
        copy_num += 1
        if copy_num == all_file_num:
            break


if __name__ == "__main__":
    main()
