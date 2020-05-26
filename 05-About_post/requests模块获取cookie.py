# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

import requests

url = "http://www.baidu.com"
response = requests.get(url)
print(type(response.cookies))

cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies)
