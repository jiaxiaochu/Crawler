# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
import requests, json
from bs4 import BeautifulSoup

start_url = "http://product.m.dangdang.com/product.php?pid=24047480&host=product.dangdang.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
}
response = requests.get(url=start_url, headers=headers)
response.encoding = response.apparent_encoding
print(response.status_code, response.encoding)
soup = BeautifulSoup(response.text, 'html.parser')
# datas = soup.find('div', class_="new_style").find('div', class_="new_left").find('span', class_="discount").text
datas = soup.find('span', class_="discount").text
# print(datas, type(datas))
new_discount = datas.replace('(', '').replace(')', '').replace('折', '')
# print(new_discount, type(new_discount))
new_new_discount = float(new_discount)
print("折扣:{}".format(new_new_discount), type(new_new_discount))

# author = soup.find('section', class_="detail j_detail").find('article', class_="dangdang_icon").text
book_name = soup.find('article', class_="dangdang_icon").text
print("书名：%s" % book_name)

author = soup.find('span', class_="linkto_value").text.replace(' ', '').replace('\n', '')
# print("作者：{}".format(author))

# publish_info = soup.find('div', class_="arrow link_line").find('span', class_="linkto_value").text. \
#     replace(' ', '').replace('\n', '')
publish_info = soup.find('a', dd_name="出版社查看作品").find('span', class_="linkto_value").text
print("出版社：{}".format(publish_info))

# infos = soup.find_all('section', class_="jump linkto_author_bang")
# for info in infos:
#     author = soup.find('span', class_="linkto_value").text.replace(' ', '').replace('\n', '')
#     print("作者：{}".format(author))
#     publish_info = soup.find('a', dd_name="出版社查看作品").find('span', class_="linkto_value").text
#     # replace(' ', '').replace('\n', '')
#     print("出版社：{}".format(publish_info))


# 优惠价
main_price = soup.find('span', class_="main_price").text
print("优惠价：{}".format(main_price))

# 定价
original_price = soup.find('div', class_="original_price").find('span').text.replace('¥', '').replace('\n', '')
print("定价：{}".format(original_price), type(original_price))

# 手动计算优惠价格（定价*折扣）
auto_price = (new_new_discount * 0.1) * float(original_price)
print("手动计算优惠价格（定价*折扣）:{:.2f}".format(auto_price))

classfiy = soup.find('span', class_="linkto_value category_text").text
print("分类信息：{}".format(classfiy))
