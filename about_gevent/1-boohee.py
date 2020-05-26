# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

# 爬取前4个常见事务分类的前4页的事食物数据信息
from gevent import monkey

monkey.patch_all()
from gevent.queue import Queue
import requests, gevent
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
}
# 前4个常见事务分类的前4页的食物数据信息
# start_url = "http://www.boohee.com/food/group/1?page=2"
start_url = "http://www.boohee.com/food/group/{num}?page={page}"
# response = requests.get(url=start_url, headers=headers)
# 我们分析完请求接口之后，现在需要根据请求结构的变化规律，手动的构造我们爬取数据所需要的请求接口
work = Queue()

for x in range(1, 5):
    for y in range(1, 5):
        real_url = start_url.format(num=x, page=y)
        # print(real_url)
        work.put_nowait(real_url)

# 第11个常见食物分类的前3页的食物记录的网址：
url_2 = 'http://www.boohee.com/food/view_menu?page={page}'
for i in range(1, 5):
    real_url = url_2.format(page=i)
    work.put_nowait(real_url)

# print(work.qsize())
