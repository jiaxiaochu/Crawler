# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

import requests, time
import pandas as pd
from bs4 import BeautifulSoup


def get_content(url, headers):
    try:
        response = requests.get(url, headers)
        # response.raise_for_status()
        # response.encoding = response.apparent_encoding
    except Exception as e:
        print("爬虫请求{}响应错误".format(i for i in range(1, 26)))
    else:
        print("爬虫请求%d响应成功" % i for i in range(1, 26))
        # response = response.text
        return response.text


def parser_content(html_content):
    # 利用BeautifulSoup将获取到的文本解析成HTML
    soup = BeautifulSoup(html_content, 'lxml')
    # 获取网页中的畅销书信息
    book_list = soup.find('ul', class_="bang_list clearfix bang_list_mode").find_all('li')
    for book in book_list:
        # info = book.find_all('div')
        # print(info)
        name = book.find('div', class_="name").find('a')['title']
        author = book.find('div', class_="publisher_info").find('a')['title']
        price = book.find('div', class_="price").find('span', class_="price_n").text
        print("书名：{};\t作者：{};\t价格：{}".format(name, author, price))
        mv_info.append([name, author, price])
        # print(item)
        # return mv_info
    # df = pd.DataFrame(item, columns=['name', 'author', 'price'])
    # print(df)
    # df.to_csv("./dangdang_book.csv", index=False)


def save_to_excel(data):
    df = pd.DataFrame(data, columns=['书名', '作者', '价格'])
    df.to_csv("./dangdang_books.csv", index=False)


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    url_list = ["http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-%d" % i for i in
                range(1, 3)]
    # 统计该爬虫的消耗时间
    print("#" * 66)
    start_time = time.time()
    # 用于存储书本信息
    mv_info = []
    for url in url_list:
        content = get_content(url, headers)
        parser_content(content)
    # print(mv_info)
    save_to_excel(mv_info)
    end_time = time.time()
    expend_time = end_time - start_time
    print("爬虫运行总共耗时{}".format(expend_time))
    print("#" * 66)
