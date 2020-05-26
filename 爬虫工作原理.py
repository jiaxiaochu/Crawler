# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

# 1.获取数据
# 2.解析数据
# 3.提取数据
# 4.存储数据


'''
1.导入需要的相关爬虫工具包/库
2.设置浏览器请求头、对应请求的网址url(数据源)、cookie、token、ip...等
3.获取响应数据、对应请求的网址数据
4.解析想要爬取的数据所在位置、分析对应数据所在的前端页面标签
5.从解析的数据中提取出想要的数据、数据转换
6.存储数据：文件、数据库...等
'''
# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get("https://www.baidu.com/")
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')   # 把网页解析为BeautifulSoup对象
# # print(soup)

import requests

response = requests.get('https://translate.google.cn/')
print(response.text)
print(response.content)
print(response.request.headers)
print(response.headers)
print(response.content.decode())
'''
访问response响应对象有三种方法：
            text  一般文本
            content   以字节的方式响应对象，遇到图片的时候，我们可以使用
            json  它是requests内置的json解码器，将json字符串解码成为字典
'''

'''
response.text 和response.content的区别

response.text
类型：str
解码类型： 根据HTTP 头部对响应的编码作出有根据的推测，推测的文本编码
如何修改编码方式：response.encoding=”gbk”

response.content
类型：bytes
解码类型： 没有指定
如何修改编码方式：response.content.deocde(“utf8”)
获取网页源码的通用方式：

response.content.decode()
response.content.decode("GBK")
response.text
以上三种方法从前往后尝试，能够100%的解决所有网页解码的问题

所以：更推荐使用response.content.deocde()的方式获取响应的html页面
'''
