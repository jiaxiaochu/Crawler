# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
# 利用多协程和队列，来爬取豆瓣图书Top250（书名，作者，评分）并存储csv 豆瓣图书
# gevent    Queue
# book_name author(publish)  score   ——>   豆瓣图书.csv
# https://book.douban.com/top250?start=0
# https://book.douban.com/top250?start=25
# https://book.douban.com/top250?start=50
# https://book.douban.com/top250?start=75
# https://book.douban.com/top250?start=225

# ?start=0

# 从gevent库里导入monkey模块
from gevent import monkey

# monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步。
monkey.patch_all()
import requests, csv
import gevent
from gevent.queue import Queue
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
}
# start_url = "https://book.douban.com/top250"
url_list = []
# 创建队列对象，并赋值给work
work = Queue()

csv_file = open('books2.csv', 'w')
writer = csv.writer(csv_file)

# 爬取前三页的数据
for i in range(3):
    url = "https://book.douban.com/top250?start=" + str(i * 25)
    url_list.append(url)
for url in url_list:
    # 用put_nowait()函数可以把网址都放进队列里
    work.put_nowait(url)


def crawler():
    # 解析提取数据
    while not work.empty():  # 当队列不是空的时候，就执行下面的程序
        url = work.get_nowait()  # 用get_nowait()函数可以把队列里的网址都取出
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        # print(response)
        bs_data = BeautifulSoup(response.text, 'html.parser')
        datas = bs_data.find_all('tr', class_="item")
        for data in datas:
            book_name = data.find_all('a')[1]['title']
            book_author = data.find('p', class_="pl").text
            book_score = data.find('span', class_="rating_nums").text
            print(book_name, book_author, book_score)
            writer.writerow([book_name, book_author, book_score])


# [< / a >, < a href = "https://book.douban.com/subject/1770782/"onclick = "&quot;moreurl(this,{i:'0'})&quot;"title = "追风筝的人" >追风筝的人< / a >]
# < a href = "https://book.douban.com/subject/1770782/"onclick = "&quot;moreurl(this,{i:'0'})&quot;"title = "追风筝的人" >追风筝的人< / a >


# 创建协程任务
task_list = []  # 创建空的任务列表
for i in range(3):  # 相当于创建了3个爬虫
    task = gevent.spawn(crawler)  # 用gevent.spawn()函数创建执行crawler()函数的任务
    task_list.append(task)  # 往任务列表添加任务。

# 用gevent.joinall方法，执行任务列表里的所有任务，就是让爬虫开始爬取网站
gevent.joinall(task_list)
