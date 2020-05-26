# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
from multiprocessing import Process
import time, os


def run_proc():
    '''子进程要执行的代码'''
    print("子进程中,pid=%d..." % os.getppid())  # os.getpid获取当前进程的进程号
    print("子进程将要结束...")


if __name__ == '__main__':
    print("父进程,pid=%d..." % os.getppid())  # os.getpid获取当前进程的进程号
    p = Process(target=run_proc)
    p.start()



""":arg
Process语法结构如下：
Process([group [, target [, name [, args [, kwargs]]]]])

target：如果传递了函数的引用，可以任务这个子进程就执行这里的代码
args：给target指定的函数传递的参数，以元组的方式传递
kwargs：给target指定的函数传递命名参数
name：给进程设定一个名字，可以不设定
group：指定进程组，大多数情况下用不到
Process创建的实例对象的常用方法：

start()：启动子进程实例（创建子进程）
is_alive()：判断进程子进程是否还在活着
join([timeout])：是否等待子进程执行结束，或等待多少秒
terminate()：不管任务是否完成，立即终止子进程
Process创建的实例对象的常用属性：

name：当前进程的别名，默认为Process-N，N为从1开始递增的整数
pid：当前进程的pid（进程号）
"""
