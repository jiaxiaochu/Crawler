# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
import requests
import json

# 引入requests和json模块。
session = requests.session()
url = 'https://xiaoke.kaikeba.com/example/wordpress/wp-login.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
data = {
    'log': input('请输入你的账号:'),
    'pwd': input('请输入你的密码:'),
    'wp-submit': '登录',
    'redirect_to': 'https://xiaoke.kaikeba.com/example/wordpress/2019/10/17/%e5%bc%80%e8%af%be%e5%90%a7%e6%97%a0%e6%95%8c%e5%a5%bd%e5%90%83%e7%9a%84%e9%a3%9f%e5%a0%82%e4%b8%80%e5%91%a8%e8%8f%9c%e8%b0%b1/',
    'testcookie': '1'
}
session.post(url, headers=headers, data=data)

cookie_dict = requests.utils.dict_from_cookiejar(session.cookies)
# 把cookie转化成字典。
print(cookie_dict)
# 打印cookie_dict
cookie_str = json.dumps(cookie_dict)
# 调用json模块的dumps函数，把cookie从字典再转成字符串。
print(cookie_str)
# 打印cookie_str
f = open('cookie.txt', 'w')
# 创建名为cookie.txt的文件，以写入模式写入内容。
f.write(cookie_str)
# 把已经转成字符串的cookie写入文件。
f.close()
# 关闭文件。
