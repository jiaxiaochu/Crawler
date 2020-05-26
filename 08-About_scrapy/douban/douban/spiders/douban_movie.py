# -*- coding: utf-8 -*-
# www.jiazhixiang.xyz  环境配置

import scrapy
from bs4 import BeautifulSoup
from ..items import MyspiderItem


class DoubanMovieSpider(scrapy.Spider):
    # 是每个项目唯一名字，用于区分不同Spider。
    name = 'douban_movie'  # 这是scrapy爬虫程序的唯一标识
    # 它是允许爬取的域名，如果初始或后续的请求链接不是这个域名，则请求链接会被过滤掉
    allowed_domains = ['https://movie.douban.com']  # 允许爬取的域名（url）范围
    start_urls = ['https://movie.douban.com/chart']  # 爬虫程序最开始（起始）爬取的url,
    # 它包含了Spider在启动时爬取的URL列表，初始请求是由它来定义的。

    # parse  解析提取
    def parse(self, response):  # 调用start_urls链接请求下载执行后则调用parse方法，并将结果传入此方法。
        bs_data = BeautifulSoup(response.text, 'html.parser')
        elements = bs_data.find_all('div', class_="pl2")
        for element in elements:
            # name,url,informations,rating
            item = MyspiderItem()
            item['movie_name'] = element.find('a').text.replace(' ', '').replace('\n', '')
            item['url'] = element.find('a')['href']
            item['information'] = element.find('p', class_="pl").text.replace(' ', '').replace('/', '@')
            item['rating'] = element.find('span', class_="rating_nums").text
            yield item

# {'movie_name': '\n'
#                '                        好莱坞往事\n'
#                '                        / 从前，有个荷里活(港) / 从前，有个好莱坞...(台)\n'}

# {'movie_name': '\n好莱坞往事\n/从前，有个荷里活(港)/从前，有个好莱坞...(台)\n'}

# {'movie_name': '好莱坞往事/从前，有个荷里活(港)/从前，有个好莱坞...(台)'}

# {'movie_name': '好莱坞往事/从前，有个荷里活(港)/从前，有个好莱坞...(台)',
#  'url': 'https://movie.douban.com/subject/27087724/'}

# {'information': '2019-05-21(戛纳电影节) / 2019-07-26(美国) / 2019(中国大陆) / 莱昂纳多·迪卡普里奥 '
#                 '/ 布拉德·皮特 / 玛格特·罗比 / 埃米尔·赫斯基 / 玛格丽特·库里 / 蒂莫西·奥利芬特 / 茱莉亚·巴特斯 / '
#                 '奥斯汀·巴特勒 / 达科塔·范宁 / 布鲁斯·邓恩 /...',
#  'movie_name': '好莱坞往事/从前，有个荷里活(港)/从前，有个好莱坞...(台)',
#  'url': 'https://movie.douban.com/subject/27087724/'}

# {'information': '2019-05-21(戛纳电影节)/2019-07-26(美国)/2019(中国大陆)/莱昂纳多·迪卡普里奥/布拉德·皮特/玛格特·罗比/埃米尔·赫斯基/玛格丽特·库里/蒂莫西·奥利芬特/茱莉亚·巴特斯/奥斯汀·巴特勒/达科塔·范宁/布鲁斯·邓恩/...',
#  'movie_name': '好莱坞往事/从前，有个荷里活(港)/从前，有个好莱坞...(台)',
#  'url': 'https://movie.douban.com/subject/27087724/'}

# {'information': '2019-05-21(戛纳电影节)@2019-07-26(美国)2019(中国大陆)莱昂纳多·迪卡普里奥布拉德·皮特玛格特·罗比埃米尔·赫斯基玛格丽特·库里蒂莫西·奥利芬特茱莉亚·巴特斯奥斯汀·巴特勒达科塔·范宁布鲁斯·邓恩...',
#  'movie_name': '好莱坞往事/从前，有个荷里活(港)/从前，有个好莱坞...(台)',
#  'url': 'https://movie.douban.com/subject/27087724/'}

# {'information': '2019-05-21(戛纳电影节)@2019-07-26(美国)@2019(中国大陆)@莱昂纳多·迪卡普里奥@布拉德·皮特@玛格特·罗比@埃米尔·赫斯基@玛格丽特·库里@蒂莫西·奥利芬特@茱莉亚·巴特斯@奥斯汀·巴特勒@达科塔·范宁@布鲁斯·邓恩@...',
#  'movie_name': '好莱坞往事/从前，有个荷里活(港)/从前，有个好莱坞...(台)',
#  'url': 'https://movie.douban.com/subject/27087724/'}

# {'information': '2019-05-21(戛纳电影节)@2019-07-26(美国)@2019(中国大陆)@莱昂纳多·迪卡普里奥@布拉德·皮特@玛格特·罗比@埃米尔·赫斯基@玛格丽特·库里@蒂莫西·奥利芬特@茱莉亚·巴特斯@奥斯汀·巴特勒@达科塔·范宁@布鲁斯·邓恩@...',
#  'movie_name': '好莱坞往事/从前，有个荷里活(港)/从前，有个好莱坞...(台)',
#  'rating': <span class="rating_nums">7.3</span>,
#  'url': 'https://movie.douban.com/subject/27087724/'}


# {'information': '2019-05-21(戛纳电影节)@2019-07-26(美国)@2019(中国大陆)@莱昂纳多·迪卡普里奥@布拉德·皮特@玛格特·罗比@埃米尔·赫斯基@玛格丽特·库里@蒂莫西·奥利芬特@茱莉亚·巴特斯@奥斯汀·巴特勒@达科塔·范宁@布鲁斯·邓恩@...',
# #  'movie_name': '好莱坞往事/从前，有个荷里活(港)/从前，有个好莱坞...(台)',
# #  'rating': '7.3',
# #  'url': 'https://movie.douban.com/subject/27087724/'}




# class MyspiderItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()  # 样列
#     movie_name = scrapy.Field()  # 电影名字
#     url = scrapy.Field()  # 电影详情链接
#     information = scrapy.Field()  # 电影的详情信息   导演  演员
#     rating = scrapy.Field()       # 电影的评分信息
