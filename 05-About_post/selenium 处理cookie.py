# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
from selenium import webdriver

driver = webdriver.Chrome()
# # 把cookie转化为字典
# {cookie[‘name’]: cookie[‘value’] for cookie in driver.get_cookies()}
# # 删除一条cookie
# driver.delete_cookie("CookieName")
# # 删除所有的cookie
# driver.delete_all_cookies()
