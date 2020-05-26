# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

import requests, time

start_time = time.time()
url_list = [
    # 'https://www.google.com/',
    'https://www.baidu.com/',
    'https://www.sina.com.cn/',
    'https://www.json.cn/',
    'https://www.qq.com/',
    'https://www.163.com/',
]

for url in url_list:
    response = requests.get(url)
    print("当前请求的网址是：{}，请求状态：{}".format(url, response.status_code))

end_time = time.time()
print("请求所用时间：%s" % (end_time - start_time))
