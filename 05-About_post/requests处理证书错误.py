# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

# import requests
#
# url = "https://www.12306.cn/mormhweb/"
# response = requests.get(url)


import requests

url = "https://www.12306.cn/mormhweb/"
response = requests.get(url, verify=False)
