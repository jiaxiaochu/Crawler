# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

# 爬取前4个常见食物分类的前4页的事食物数据信息
from gevent import monkey

# 让程序变成异步模式
# 从gevent库里导入monkey模块
# monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步。
monkey.patch_all()
from gevent.queue import Queue
import requests, gevent
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
}
# 前4个常见事务分类的前4页的事食物数据信息
# start_url = "http://www.boohee.com/food/group/1?page=2"
start_url = "http://www.boohee.com/food/group/{num}?page={page}"
# response = requests.get(url=start_url, headers=headers)

work = Queue()

# 通过两个for循环，能设置分类的数字和页数的数字
# 前3个分类的前4页的食物记录的网址：
for x in range(1, 5):
    for y in range(1, 5):
        real_url = start_url.format(num=x, page=y)
        work.put_nowait(real_url)
        # 通过for循环，能设置第11个常见食物分类的食物的页数。
        # 然后，把构造好的网址用put_nowait方法添加进队列里。

# 第11个常见食物分类的前3页的食物记录的网址：
url_2 = 'http://www.boohee.com/food/view_menu?page={page}'
for i in range(1, 5):
    real_url = url_2.format(page=i)
    work.put_nowait(real_url)  # 然后，把构造好的网址用put_nowait方法添加进队列里


def crawler(*args):
    while not work.empty():  # 当队列不是空的时候，就执行下面的程序
        url = work.get_nowait()  # 用get_nowait()方法从队列里把刚刚放入的网址提取出来
        response = requests.get(url=url, headers=headers)
        bs_data = BeautifulSoup(response.text, 'html.parser')
        food = bs_data.find_all(class_="item clearfix")
        for food in food:
            food_name = food.find_all('a')[1]['title']
            food_url = 'http://www.boohee.com' + food.find_all('a')[1]['href']
            food_calorie = food.find('p').text
            print(food_name, food_url, food_calorie)


task_list = []
for i in range(1, 5):  # 相当于创建了5个爬虫
    # 用gevent.spawn()函数创建执行crawler()函数的任务
    task = gevent.spawn(crawler)
    task_list.append(task)

# 用gevent.joinall方法，启动协程，执行任务列表里的所有任务，让爬虫开始爬取网站
gevent.joinall(task_list)
# print(work.qsize())
