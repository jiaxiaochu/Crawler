# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
# 本地Chrome浏览器设置方法
# 引入Webdriver
from selenium import webdriver
import time

# 声明Chrome浏览器  # 设置引擎为Chrome，从本地打开一个Chrome浏览器
driver = webdriver.Chrome()
# 用get方法打开
driver.get('https://xiaoke.kaikeba.com/example/X-Man/')
# html = driver.page_source
# print(html)
time.sleep(2)  # 延时操作
teacher = driver.find_element_by_id('teacher')
teacher.send_keys('开课吧')

assistant = driver.find_element_by_name('assist')
assistant.send_keys('全都喜欢')

time.sleep(2)
button = driver.find_element_by_tag_name('button')
time.sleep(1)
button.click()
time.sleep(5)
driver.close()
# from selenium import  webdriver #从selenium库中调用webdriver模块
# from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
#
# chrome_options = Options() # 实例化Option对象
# chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
# driver = webdriver.Chrome(options = chrome_options) # 设置引擎为Chrome，在后台默默运行
