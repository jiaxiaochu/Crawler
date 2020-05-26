# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang


'''
全局解释锁(GIL)
在Python的原始解释器Cpython中存在着GIL(Global Interpreter Lock,全局解释器锁锁)，
因此在解释器执行Python代码时，会产生互斥锁来限制线程对共享资源的访问，直到解释器遇到I/O操作或者达到一定数目时才会释放GIL。

由于全局解释器锁的存在，在进行多线程操作的时候，不能调用多个CPU内核，只能利用一个内核，
所以在进行CPU密集型操作的时候，不推荐使用多线程，更加倾向于多进程。

那么多线程适合什么样的应用场景呢？
对于IO密集型的操作，多线程可以明显提高效率，列如Python爬虫的开发，绝大多数时间爬虫是在等待socket返回数据，网络IO的操作延迟比CPU大得多。

'''
import keyword
print(keyword.kwlist)
