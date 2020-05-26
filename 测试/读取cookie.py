# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
import requests
import json

session = requests.session()
# 创建会话。
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
# 添加请求头，避免被反爬虫。
try:
    # 如果能读取到cookie文件，执行以下代码，跳过except的代码，不用登录就能发表评论。
    cookie_txt = open('cookie_kaikeba.txt', 'r')
    # 以reader读取模式，打开名为cookie.txt的文件。
    cookie_dict = json.loads(cookie_txt.read())
    # 调用json模块的loads函数，把字符串转成字典。
    cookie = requests.utils.cookiejar_from_dict(cookie_dict)
    # 把转成字典的cookie再转成cookie本来的格式。
    session.cookies = cookie
# 获取cookie：就是调用requests对象（session）的cookie属性。

except FileNotFoundError:
    # 如果读取不到cookie文件，程序报“FileNotFoundError”（找不到文件）的错，则执行以下代码，重新登录获取cookie，再评论。
    print("存储cookie的文件不存在")
    url = 'https://xiaoke.kaikeba.com/example/wordpress/wp-login.php'
    # 登录的网址。
    data = {'log': input('请输入你的账号:'),
            'pwd': input('请输入你的密码:'),
            'wp-submit': '登录',
            'redirect_to': 'https://xiaoke.kaikeba.com/example/wordpress/2019/10/17/%e5%bc%80%e8%af%be%e5%90%a7%e6%97%a0%e6%95%8c%e5%a5%bd%e5%90%83%e7%9a%84%e9%a3%9f%e5%a0%82%e4%b8%80%e5%91%a8%e8%8f%9c%e8%b0%b1/',
            'testcookie': '1'}
    # 登录的参数。
    session.post(url, headers=headers, data=data)
    # 在会话下，用post发起登录请求。

    cookie_dict = requests.utils.dict_from_cookiejar(session.cookies)
    # 把cookie转化成字典。
    cookie_str = json.dumps(cookie_dict)
    # 调用json模块的dump函数，把cookie从字典再转成字符串。
    f = open('cookie_kaikeba.txt', 'w')
    # 创建名为cookie.txt的文件，以写入模式写入内容
    f.write(cookie_str)
    # 把已经转成字符串的cookie写入文件
    f.close()
# 关闭文件
url_comment = 'https://xiaoke.kaikeba.com/example/wordpress/wp-comments-post.php'
# 文章的网址。
data_comment = {
    'comment': input('请输入你想要发表的评论：'),
    'submit': '发表评论',
    'comment_post_ID': '35',
    'comment_parent': '0'
}
# 评论的参数。
comment = session.post(url_comment, headers=headers, data=data_comment)
# 在创建的session下用post发起评论请求，放入参数：文章网址，请求头和评论参数，并赋值给comment。
print(comment.status_code)
# 打印comment的状态码
