# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

start_url = "http://www.weather.com.cn/weather/101280601.shtml"
res = requests.get(url=start_url, headers=headers)
res.encoding = 'utf-8'
bs_data = BeautifulSoup(res.text, 'html.parser')
data1 = bs_data.find(class_="wea")
data2 = bs_data.find(class_="tem")
print(data1.text, data2.text)

