# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
""":arg
work = Queue()实例化一个队列，可以传入参数，如Queue(10)表示队列只能存储10个成员。
work.put_nowait(url)表示：添加队列的成员
while not work.empty():表示：当这个队列不为空时
url = work.get_nowait()表示：取出队列的成员
work.qsize()表示:队列的长度
tasks_list = [gevent.spawn(crawler) for x in range(2)]相当于创建2个爬虫执行crawler()函数
gevent.joinall(tasks_list)启动所有任务


put_nowait()    # 往队列里存储数据
get_nowait()    # 从队列里取出数据
empty()         # 判断队列是否为空
full()          # 判断队列是否为满
qsize()         # 判断队列还剩多少数量
"""

from gevent import monkey

monkey.patch_all()  # monkey模块，这个模块能将程序转换成可异步的程序
from gevent.queue import Queue
import requests, time, gevent

start_time = time.time()
url_list = [
    'https://www.baidu.com/',
    'https://www.sina.com.cn/',
    'http://www.sohu.com/',
    'https://www.qq.com/',
    'https://www.163.com/',
    'http://www.iqiyi.com/',
    'https://www.tmall.com/',
    'http://www.ifeng.com/'
]
# 创建Queue对象（任务队列）
work = Queue()

# 将请求任务(连接)放入Queue队列当中
for url in url_list:
    work.put_nowait(url)


# 请求数据
def crawler():
    # 判断任务队列是否为空（判断任务队里当中是否有任务）
    while not work.empty():
        # 将请求任务(连接)从Queue队列当中取出来
        url = work.get_nowait()
        response = requests.get(url)
        print("当前请求的网址是：{}，请求状态：{},剩余任务数量：{}".format(url, response.status_code, work.qsize()))


# 创建任务列表
task_list = []
for i in range(2):
    # 用gevent.spawn()函数创建执行crawler()函数的任务。
    task = gevent.spawn(crawler)
    # 往任务列表添加任务。
    task_list.append(task)

# 用gevent.joinall方法，执行任务列表里的所有任务，就是让爬虫开始爬取网站。
gevent.joinall(task_list)
end_time = time.time()
print("请求所用时间：%s" % (end_time - start_time))
