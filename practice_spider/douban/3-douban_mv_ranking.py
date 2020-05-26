# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

import requests
# 引用requests库
from bs4 import BeautifulSoup

# 引用BeautifulSoup库
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
res_movies = requests.get('https://movie.douban.com/chart', headers=headers)
# 获取数据
bs_movies = BeautifulSoup(res_movies.text, 'html.parser')
# 解析数据
list_movies = bs_movies.find_all('div', class_='pl2')
# print(list_movies)
# 查找最小父级标签
# tag_p = list_movies[0].find('p')
# tag_p = list_movies[0].find('div', class_='star clearfix')
# print(tag_p)
# print(tag_p.text)
# # 提取第0个父级标签中的<p>标签
# information = tag_p.text.replace(' ', '').replace('\n', '')
# # 电影基本信息，使用replace方法去掉多余的空格及换行符
#
# print('电影的基本信息为：' + information)
# 输出结果

# 创建一个空列表，用于存储信息
list_all = []
for movie in list_movies:
    tag_a = movie.find('a')
    # 电影名
    name = tag_a.text.replace(' ', '').replace('\n', '')
    # 电影节
    url = tag_a['href']
    # 电影详情
    tag_p = movie.find('p', class_='pl')
    mv_information = tag_p.text.replace(' ', '').replace('\n', '')
    # 电影评分
    tag_div = movie.find('div', class_="star clearfix")
    rating = tag_div.text.replace(' ', '').replace('\n', '')
    list_all.append([name, url, mv_information, rating])
    print(list_all)
