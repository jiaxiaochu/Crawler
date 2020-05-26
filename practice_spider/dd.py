import requests
from lxml import etree

url = "http://product.dangdang.com/24047480.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"
}
r = requests.get(url, headers=headers)
c = r.content.decode(encoding="gbk")
print(r.status_code)
html = etree.HTML(c)
print(html)
# print(type(html))
book_name = html.xpath('//*[@id="breadcrumb"]/span[5]')
# book_name2 = html.xpath('//*[@id="breadcrumb"]')
# print(book_name)
# book_Author = html.xpath('//*[@id="author"]/a[2]')
# book_press = html.xpath('//*[@id="product_info"]/div[2]/span[2]/a')
# book_youhuijia = html.xpath('//*[@id="dd-price"]/text()')
# book_dingjia = html.xpath('//*[@id="original-price"]/text()')
# book_time = html.xpath('//*[@id="product_info"]/div[2]/span[3]')
# book_3 = html.xpath('//*[@id="breadcrumb"]/a[4]')
# book_2 = html.xpath('//*[@id="breadcrumb"]/a[3]')
# book_1 = html.xpath('//*[@id="breadcrumb"]/a[2]')
# book_ISBN = html.xpath('//*[@id="detail_describe"]/ul/li[5]')
# print("图书名：" + book_name)
# print("作者：" + book_Author)
# print("出版社：" + book_press)
# print("优惠价：" + book_youhuijia)
# print("定价：" + book_dingjia)
# print("出版时间：" + book_time)
# print("三级分类：" + book_3)
# print("二级分类：" + book_2)
# print("一级分类：" + book_1)
# print("ISBN号：" + book_ISBN)
