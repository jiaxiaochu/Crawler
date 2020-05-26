# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
import requests
from bs4 import BeautifulSoup

start_url = "http://product.dangdang.com/24047480.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
}
response = requests.get(url=start_url, headers=headers)
response.encoding = response.apparent_encoding
print(response.status_code, response.encoding)
soup = BeautifulSoup(response.text, 'html.parser')
datas = soup.find_all('div', id="product_info")
author_info = soup.find_all('span', id='author')

for data in datas:
    book_name = data.find('div', class_="name_info").find('h1')['title']  # .replace(' ', '').replace('\n', '')
    # book_author1 = data.find('span', id="author").find('a', target="_blank")
    book_publish_info = data.find('span', dd_name="出版社").text
    # book_publish_time = data.find('span', class_="messbox_info")
    print("书名：{},出版社：{}".format(book_name, book_publish_info))

# print(author_info)
# [<span class="t1" dd_name="作者" ddt-area="002" id="author">作者:[德]<a dd_name="作者" href="http://search.dangdang.com/?key2=%BA%BA%CB%B9&amp;medium=01&amp;category_path=01.00.00.00.00.00" target="_blank">汉斯</a>-<a dd_name="作者" href="http://search.dangdang.com/?key2=%B8%F1%B0%C2%B6%FB%B8%F1%A1%A4%D9%A4%B4%EF%C4%AC%B6%FB&amp;medium=01&amp;category_path=01.00.00.00.00.00" target="_blank">格奥尔格・伽达默尔</a> 著，<a dd_name="作者" href="http://search.dangdang.com/?key2=%BA%E9%BA%BA%B6%A6&amp;medium=01&amp;category_path=01.00.00.00.00.00" target="_blank">洪汉鼎</a> 译</span>]

for item in author_info:
    author1 = item.find_all('a', target="_blank")[0].text
    author2 = item.find_all('a', target="_blank")[1].text
    author3 = item.find_all('a', target="_blank")[2].text
    print("作者：{}".format(author1 + author2 + author3))
# print(author_info)
# print(datas)


price_info = soup.find('div', class_="price_pc", id="pc-price")
# print(price_info)
# 定价
origin_price = price_info.find('div', class_="price_m", id="original-price").text
# print("定价：{}".format(origin_price))
# 刷新页面瞬间变化值price
p_price = price_info.find('div', class_="price_d").find('p', id="dd-price").text
# print("刷新页面瞬间变化价格：{}".format(p_price))
# 折扣
discount = price_info.find('div', class_="price_zhe", id="dd-zhe").text
# print("折扣：{}".format(discount))
# 刷新页面瞬间变化值price
# price = data.find('div', class_="price_d").find('p', id="dd-price").text
print("定价：{}".format(origin_price))
print("刷新页面瞬间变化价格：{}".format(p_price))
print("折扣：{}".format(discount))

classify = datas.find('div', class_="breadcrumb", id="breadcrumb", dd_name="顶部面包屑导航")
print(classify)
for sort in classify:
    c1 = sort.find_all('a')[0].text
    print("一级分类：{}".format(c1))

# for data in datas:
#     book_name = data.find('div', class_="name_info").find('h1')['title']  # .replace(' ', '').replace('\n', '')
#     # book_author1 = data.find('span', id="author").find('a', target="_blank")
#     book_publish_info = data.find('span', dd_name="出版社").text
#     book_publish_time = data.find('span', class_="messbox_info")
#     print(book_publish_time)
#     classify = data.find('div', class_="breadcrumb", id="breadcrumb").find()
# price = data.find('div', class_="price_d").find('span', class_="yen").text
# 定价
# origin_price = data.find('div', class_="price_m", id="original-price").text
# discount = data.find('div', class_="price_d").find('div', class_="price_zhe", id="dd-zhe")
# print(discount)
# 刷新页面瞬间变化值price
# price = data.find('div', class_="price_d").find('p', id="dd-price").text
# print(book_name, book_publish_info, origin_price)
