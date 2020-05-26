# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

# 在遇到页面交互复杂或是URL加密逻辑复杂的情况时，selenium就派上了用场，它可以真实地打开一个浏览器，
# 等待所有数据都加载到Elements中之后，再把这个网页当做静态网页爬取就好了。
# 但是，使用selenium时，当然也有美中不足之处；
# 由于要真实地运行本地浏览器，打开浏览器以及等待网渲染完成需要一些时间，
# selenium的工作不可避免地牺牲了速度和更多资源，不过，至少不会比人慢。


# 本地Chrome浏览器设置方法
from selenium import webdriver #从selenium库中调用webdriver模块
driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器


# Selenium元素定位的30种方式
# https://blog.csdn.net/qq_32897143/article/details/80383502
