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


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
start_url = "https://movie.douban.com/top250"
response = requests.get(url=start_url, headers=headers)
response.encoding = response.apparent_encoding
# print(response)
html = etree.HTML(response.content)
path = '//*[@id="content"]/div/div[1]/ol/li[1]/div'
books = html.xpath('//div[@class="item"]')  # 相对路径  相当于//*[@id="content"]/div/div[1]/ol/li[2]/div
for book in books:
    # book_name = book.xpath('.//a/span/text()')#[0].strip()  # 相对路径
    # book_title1 = book.xpath('./div[2]/div[1]/a/span[2]/text()')[0].strip()  # 相对路径
    # book_title2 = book.xpath('.//a/span[@class="other"]/text()')  # 相对路径
    # infomation = book.xpath('.//p[1]/text()')
    # infomations = book.xpath('./div[2]/div[2]/p[1]/text()[2]')
    # print(infomations)
    # print(info(infomations)
    # print(info(book_name))
    # print(info(book_title1).replace("/", "").replace(" ", ""))
    # print(info(book_title2).replace("/", "").replace(" ", ""))
    # try:
    #     book_info = book.xpath('.//a/span/text()')
    #     book_name = book_info[0]
    #     book_title1 = book_info[1].strip().replace("/", "").replace(" ", "")
    #     book_title2 = book_info[2].strip().replace("/", "").replace(" ", "")
    # except Exception as e:
    #     # print("提取数据出错")
    #     book_title2 = book_title1  # book_info[1].strip().replace("/", "").replace(" ", "")
    #     # print(book_title2)
    #     # pass
    # else:
    #     title = book_title1 + "/" + book_title2
    #     print(title)
    #     pass
    book_info = book.xpath('.//a/span/text()')
    book_name = book_info[0]
    book_title1 = book_info[1].strip().replace("/", "").replace(" ", "")
    try:
        book_title2 = book_info[2].strip().replace("/", "").replace(" ", "")
    except Exception as e:
        book_title2 = book_title1
    else:
        title = book_title1 + "/" + book_title2
        print(title)
    # try:
    #     book_info = book.xpath('.//a/span/text()')
    #     book_name = book_info[0]
    #     book_title = book_info[1:3:]
    #     print(book_title)
    # except Exception as e:
    #     print("提取数据出错")
    # else:
    #     # print(info(book_title))
    #     pass
    director_infos = book.xpath('.//p/text()')  # ./div[2]/div[2]/p[1]/text()[1]
    director_info = director_infos[0].strip() + director_infos[1].strip()
    # print(director_info)
    score = book.xpath('.//span[@class="rating_num"]/text()')[0]  # ./div[2]/div[2]/div/span[2]/text()
    # print(score)
    mv_comment_data = book.xpath('.//span[4]/text()')[0]
    # print(mv_comment_data)
    recommend = book.xpath('.//span[@class="inq"]/text()')[0]
    # print(recommend)
    link_info = book.xpath('./div[2]/div[1]/a/@href')
    link = info(link_info)
    status = book.xpath(path + '/div[2]/div[1]/span/text()')[0]  # ./div[2]/div[1]/span/text()
    # print(type(status))
    # print(book_name + title)



    # try:
    #     book_info = book.xpath('.//a/span/text()')
    #     book_name = book_info[0]
    #     director_infos = book.xpath('.//p/text()')  # ./div[2]/div[2]/p[1]/text()[1]
    #     director_info = director_infos[0].strip() + director_infos[1].strip()
    #     score = book.xpath('.//span[@class="rating_num"]/text()')[0]  # ./div[2]/div[2]/div/span[2]/text()
    #     mv_comment_data = book.xpath('.//span[4]/text()')[0]
    #     recommend = book.xpath('.//span[@class="inq"]/text()')[0]
    #     link_info = book.xpath('./div[2]/div[1]/a/@href')
    #     link = info(link_info)
    #     status = book.xpath(path + '/div[2]/div[1]/span/text()')[0]  # ./div[2]/div[1]/span/text()
    # except Exception as e:
    #     print("运行出错")
    # else:
    #     print(book_name, director_info, score, mv_comment_data, recommend, link, score)
