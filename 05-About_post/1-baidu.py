# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
}
# response = requests.post("http://www.baidu.com/", data=data, headers=headers)
# data 的形式：字典
kw = {'wd': '长城'}
response = requests.get("https://www.baidu.com/", params=kw)
