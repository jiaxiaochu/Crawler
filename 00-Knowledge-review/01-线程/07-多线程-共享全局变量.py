# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

from threading import Thread
import time

# 全局变量
g_num = 100


def work1():
    global g_num
    for i in range(3):
        g_num += 1
    print("---in work1,g_num is---%d" % g_num)


def work2():
    global g_num
    print("---in work2,g_num is---%d" % g_num)


if __name__ == '__main__':
    print("---线程创建之前g_num is %d---" % g_num)
    t1 = Thread(target=work1)
    t1.start()

    time.sleep(1)  # 延时一会，保证t1线程中的事情做完

    t2 = Thread(target=work2)
    t2.start()
""":arg
在一个进程内的所有线程共享全局变量，很方便在多个线程间共享数据
缺点就是，线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱（即非线程安全）
"""
