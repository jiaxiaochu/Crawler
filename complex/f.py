# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
import requests
from lxml import etree


# 如果提取不成功，返回空字符串，成功则取值
def info(list_name):
    if list_name == []:
        return ''
    else:
        return list_name[0]


# 用Xpath提取数据
def get_data(url, headers):
    r = requests.get(url, headers=headers)
    html = etree.HTML(r.text)
    # print(html)
    books = html.xpath('//tr[@class="item"]')
    for book in books:
        title = book.xpath('./td[2]/div[1]/a/@title')
        print(info(title))
    #     link = book.xpath('./td[2]/div[1]/a/@href')
    #     num = book.xpath('./td[2]/div[2]/span[2]/text()')
    #     introduce = book.xpath('./td[2]/p[2]/span/text()')
    #     print(info(title), info(num), info(introduce), info(link))


if __name__ == "__main__":
    for i in range(10):
        url = 'https://book.douban.com/top250?start=' + str(i * 25)
        headers = {'User-Agent': 'Mozilla/5.0'}
        get_data(url, headers)
