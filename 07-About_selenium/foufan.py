# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

from selenium import webdriver

# 创建浏览器对象
dr = webdriver.Chrome()

# 发送请求
dr.get('http://www.fanfou.com/')

# 查看源码
print(dr.title)

print(dr.page_source)

dr.save_screenshot("fanfou.png")

dr.close()
