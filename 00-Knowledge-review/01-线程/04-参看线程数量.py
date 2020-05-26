# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

import threading
from time import sleep, ctime


def sing():
    for i in range(3):
        print("正在唱歌。。。%d" % i)
        sleep(1)


def dance():
    for i in range(3):
        print("正在跳舞。。。%d" % i)
        sleep(1)


if __name__ == '__main__':
    print("---程序开始---：%s" % ctime())
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

    while True:
        length = len(threading.enumerate())
        print("当前运行的线程数为：%d" % length)
        if length <= 1:
            break

        sleep(0.5)
    print("---程序结束---：%s" % ctime())

# seq = ['one', 'two', 'three']
# for i, element in enumerate(seq):
#     print(i, element)
