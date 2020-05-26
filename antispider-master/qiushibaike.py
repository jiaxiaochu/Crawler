# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
# coding=utf-8
import requests
from lxml import etree


class QiubaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X \
        10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}

    def get_url_list(self):  # 获取url列表
        return [self.url_temp.format(i) for i in range(1, 14)]

    def parse_url(self, url):  # 发送请求，获取响应
        print(url)
        return requests.get(url, headers=self.headers).content.decode()

    def get_content_list(self, html_str):  # 提取段子
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@id='content-left']/div")
        content_list = []
        for div in div_list:
            content = {}
            content["content"] = div.xpath(".//div[@class='content']/span/text()")
            content_list.append(content)
        return content_list

    def save_content_list(self, content_list):  # 保存数据
        pass

    def run(self):
        # 1. url_list
        url_list = self.get_url_list()
        # 2. 遍历，发送请求
        for url in url_list:
            html_str = self.parse_url(url)
            # 3. 提取数据
            content_list = self.get_content_list(html_str)
            # 4. 保存
            self.save_content_list(content_list)


if __name__ == '__main__':
    qiubai = QiubaiSpider()
    qiubai.run()
