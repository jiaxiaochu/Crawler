# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ..items import JobuiItem


class InfoSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['jobui.com']
    start_urls = ['https://www.jobui.com/rank/company/']

    def parse(self, response):
        bs_data = BeautifulSoup(response.text, 'html.parser')
        lable = bs_data.find_all('ul', class_="textList flsty cfix")
        for datas in lable:
            info = datas.find_all('a')
            for data in info:
                company_id = data['href']
                link = 'https://www.jobui.com{id}jobs/'
                url = link.format(id=company_id)
                yield scrapy.Request(url, callback=self.parser_job)
                # scrapy.Request是构造requests对象的类。real_url是我们往requests对象里传入的每家公司招聘信息网址的参数。

    def parser_job(self, response):
        bs_data = BeautifulSoup(response.text, 'html.parser')
        company = bs_data.find(id="companyH1").text
        datas = bs_data.find_all('div', class_="c-job-list")
        for data in datas:
            item = JobuiItem()
            item['company'] = company
            item['position'] = data.find('h3').text
            item['address'] = data.find('span')['title']

            yield item
