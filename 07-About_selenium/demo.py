# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

import time
from selenium import webdriver

start_url = "https://localprod.pandateacher.com/python-manuscript/hello-spiderman/"

driver = webdriver.Chrome()
driver.get(url=start_url)
time.sleep(2)
username = driver.find_element_by_id('teacher')
time.sleep(1)
password = driver.find_element_by_name('assistant')
time.sleep(1)
button = driver.find_element_by_class_name('sub')
time.sleep(1)
button.click()
time.sleep(1)
driver.close()
