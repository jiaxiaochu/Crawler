# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
}

start_url = "https://www.lagou.com/jobs/list_%E5%AD%97%E8%8A%82%E8%B7%B3%E5%8A%A8?labelWords=&fromSearch=true&suginput="
# https://www.lagou.com/jobs/list_%E5%AD%97%E8%8A%82%E8%B7%B3%E5%8A%A8?labelWords=&fromSearch=true&suginput=
# https://www.lagou.com/jobs/list_%E5%AD%97%E8%8A%82%E8%B7%B3%E5%8A%A8?labelWords=&fromSearch=true&suginput=

response = requests.get(url=start_url, headers=headers)
response.encoding = response.apparent_encoding
# print(response.status_code, response.encoding)
soup = BeautifulSoup(response.text, 'html.parser')
datas = soup.find('ul', class_="item_con_list")
for data in datas:
    position = data.find('div', class_="position")
    print(position)

