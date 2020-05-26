# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.douban.com/")

ret4 = driver.find_elements_by_tag_name("h1")
print(ret4[0].text)
# 输出：豆瓣

ret5 = driver.find_elements_by_link_text("下载豆瓣 App")
print(ret5[0].get_attribute("href"))
# 输出：https://www.douban.com/doubanapp/app?channel=nimingye

driver.close()
