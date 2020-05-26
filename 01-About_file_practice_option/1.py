# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-

# 我们在第4课中爬取了豆瓣排行里的“豆瓣新片榜”的电影名，URL，电影基本信息，电影评分信息现在我们将他保存下来
# 地址：https://movie.douban.com/chart


# 1.获取数据   requests
# 2.解析数据   分析网页结构   HTMl/json
# 3.提取数据   BeautifulSoup   find/find_all   Tag.text
# 4.存储数据    openpyxl
# https://movie.douban.com/chart


import requests
from bs4 import BeautifulSoup
import csv

file = open('douan_data.csv', "a")
writer = csv.writer(file)

url = "https://movie.douban.com/chart"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}
response = requests.get(url=url, headers=headers)
if response.status_code == 200:
    print(response.status_code, "请求成功")
    # print(response.text)
    bs_response = BeautifulSoup(response.text, 'html.parser')
    movie_data = bs_response.find_all('div', class_="pl2")
    list_movie = []
    for movie in movie_data:
        # 电影名
        name = movie.find('a').text.replace(" ", "").replace("\n", "")
        # URL
        link = movie.find('a')['href']
        # 电影基本信息
        movie_info = movie.find("p", class_="pl").text
        # 电影评分
        # rating = movie.find("div", class_="star clearfix").text
        # print(rating)
        movie_rating = movie.find("span", class_="rating_nums").text
        writer.writerow([name, link, movie_info, movie_rating])
        # print(movie_rating)
        # print(name, link, movie_info, movie_rating)
        # list_movie.append([name, link, movie_info, movie_rating])
        # sheet.append([name, link, movie_info, movie_rating])
        print("数据写入中. . .")
    # print(list_movie)
    # wb.save("douban.xlsx")
    print("数据写入成功")
    # wb.close()
    file.close()
