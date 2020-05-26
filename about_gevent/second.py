# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang


from gevent import monkey  # monkey模块，这个模块能将程序转换成可异步的程序
monkey.patch_all()
import requests, time, gevent

start_time = time.time()
url_list = [
    # 'https://www.google.com/',
    'https://www.baidu.com/',
    'https://www.sina.com.cn/',
    'https://www.json.cn/',
    'https://www.qq.com/',
    'https://www.163.com/',
]


def crawler(url):
    response = requests.get(url)
    print("当前请求的网址是：{}，请求状态：{}".format(url, response.status_code))


task_list = []
for url in url_list:
    # 用gevent.spawn()函数创建执行crawler()函数的任务。
    task = gevent.spawn(crawler, url)
    task_list.append(task)  # 往任务列表添加任务。

# 用gevent.joinall方法，执行任务列表里的所有任务，就是让爬虫开始爬取网站。
gevent.joinall(task_list)
end_time = time.time()
print("请求所用时间：%s" % (end_time - start_time))
