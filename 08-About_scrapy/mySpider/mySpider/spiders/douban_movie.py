# -*- coding: utf-8 -*-
import scrapy
import bs4
from ..items import MyspiderItem


class DoubanMovieSpider(scrapy.Spider):
    name = 'douban_movie'
    allowed_domains = ['https://movie.douban.com']
    start_urls = ['https://movie.douban.com/chart']

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        elements = soup.find_all('div', class_='pl2')
        for element in elements:
            item = MyspiderItem()
            item['name'] = element.find('a').text.replace(' ', '').replace('\n', '')
            item['url'] = element.find('a')['href']
            item['information'] = element.find('p', class_='pl').text.replace(' ', '').replace('\n', '')
            item['rating'] = element.find('div', class_='star clearfix').text.replace(' ', '').replace('\n', '')
            yield item
