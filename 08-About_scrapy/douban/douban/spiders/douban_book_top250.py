# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ..items import DoubanItem


class DoubanBookTop250Spider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['book.douban.com']
    # start_urls = ['https://book.douban.com/top250?start=0']
    start_urls = []
    for i in range(3):
        url = 'https://book.douban.com/top250?start=' + str(i * 25)
        start_urls.append(url)

    def parse(self, response):
        bs_data = BeautifulSoup(response.text, 'html.parser')
        # print(response.text)
        # 用find_all提取<tr class="item">元素，这个元素里含有书籍信息。
        datas = bs_data.find_all('tr', class_="item")
        # 遍历data。
        for data in datas:
            # 实例化DoubanItem这个类。
            item = DoubanItem()
            # 提取出书名，并把这个数据放回DoubanItem类的title属性里。
            item['name'] = data.find_all('a')[1]['title']
            # 提取出出版信息，并把这个数据放回DoubanItem类的publish里。
            item['publish'] = data.find('p', class_='pl').text
            item['recommend'] = data.find('span', class_="inq")
            # 提取出评分，并把这个数据放回DoubanItem类的score属性里。
            item['score'] = data.find('span', class_='rating_nums').text
            print(item['name'], item['score'])  # 打印书名。

            # yield item是把获得的item传递给引擎。
            yield item
