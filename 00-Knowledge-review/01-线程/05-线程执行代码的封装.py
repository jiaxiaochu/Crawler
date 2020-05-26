# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

import threading, time

"""
通过使用threading模块能完成多任务的程序开发，为了让每个线程的封装性更完美，
所以使用threading模块时，往往会定义一个新的子类class，只要继承threading.Thread就可以了，然后重写run方法
"""


class MyThred(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            data = "我是线程：{a}  @  {b}".format(a=self.name, b=i)  # name属性中保存的是当前线程的名字
            print(data)


if __name__ == '__main__':
    t = MyThred()
    t.start()

# python的threading.Thread类有一个run方法，用于定义线程的功能函数，可以在自己的线程类中覆盖该方法。
# 而创建自己的线程实例后，通过Thread类的start方法，可以启动该线程，交给python虚拟机进行调度，
# 当该线程获得执行的机会时，就会调用run方法执行线程。
"""
:arg
threading.Thread类run方法官方源码
def run(self):
    # Method representing the thread's activity.
    # 
    # You may override this method in a subclass. The standard run() method
    # invokes the callable object passed to the object's constructor as the
    # target argument, if any, with sequential and keyword arguments taken
    # from the args and kwargs arguments, respectively.

    try:
        if self._target:
            self._target(*self._args, **self._kwargs)
    finally:
        # Avoid a refcycle if the thread is running a function with
        # an argument that has a member that points to the thread.
        del self._target, self._args, self._kwargs
"""
