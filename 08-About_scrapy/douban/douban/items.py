# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 定义书名的属性
    publish = scrapy.Field()  # 定义出版信息的属性
    score = scrapy.Field()  # 定义书籍的评分属性
    recommend = scrapy.Field()  # 定义书籍的推荐语属性


class DoubanCommentsItem(scrapy.Item):
    book_name = scrapy.Field()
    ID_name = scrapy.Field()
    comment = scrapy.Field()


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()  # 样列
    movie_name = scrapy.Field()  # 电影名字
    url = scrapy.Field()  # 电影详情链接
    information = scrapy.Field()  # 电影的详情信息   导演  演员
    rating = scrapy.Field()       # 电影的评分信息