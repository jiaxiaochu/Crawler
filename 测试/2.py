# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
import requests

session = requests.session()
# 用requests.session()创建session对象，相当于创建了一个特定的会话，帮我们自动保持了cookie。
url_login = 'https://xiaoke.kaikeba.com/example/wordpress/wp-login.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
data_login = {
    'log': input('请输入账号：'),  # 用input函数填写账号和密码，这样代码更优雅，而不是直接把账号密码填上去。
    'pwd': input('请输入密码：'),
    'wp-submit': '登录',
    'redirect_to': 'https://xiaoke.kaikeba.com/example/wordpress/2019/10/17/%e5%bc%80%e8%af%be%e5%90%a7%e6%97%a0%e6%95%8c%e5%a5%bd%e5%90%83%e7%9a%84%e9%a3%9f%e5%a0%82%e4%b8%80%e5%91%a8%e8%8f%9c%e8%b0%b1/',
    'testcookie': '1'
}
session.post(url_login, headers=headers, data=data_login)
# 在创建的session下用post发起登录请求，放入参数：请求登录的网址、请求头和登录参数。
url_comment = 'https://xiaoke.kaikeba.com/example/wordpress/wp-comments-post.php'
# 把我们想要评论的文章网址赋值给url_comment。
data_comment = {
    'comment': input('请输入你想要发表的评论：'),
    'submit': '发表评论',
    'comment_post_ID': '35',
    'comment_parent': '0'
}
# 把有关评论的参数封装成字典。
comment = session.post(url_comment, headers=headers, data=data_comment)
# 在创建的session下用post发起评论请求，放入参数：文章网址，请求头和评论参数，并赋值给comment。
print(comment)
# 打印comment
