# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

import requests, json

b = 'bid=Qzw9cKnyESM; ll="108288"; __yadk_uid=4YChvgeANLBEh4iV00n1tc0HQ8zpmSl1; __utmc=30149280; __utmc=223695111; _vwo_uuid_v2=D8099FF3ECFE384A3F35BFA190C05A5EE|91f795432cda34bbc17ba6265fb33177; ps=y; dbcl2="169126613:FUpqH/CNWB8"; ck=pyZ7; ap=1; push_noty_num=0; push_doumail_num=0; __utmz=30149280.1520490941.8.7.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utmv=30149280.16912; __utmz=223695111.1520492304.6.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; ct=y; __utma=30149280.1712477244.1514880643.1520490941.1520496097.9; __utmb=30149280.0.10.1520496097; __utma=223695111.1169484511.1516955420.1520492304.1520496097.7; __utmb=223695111.0.10.1520496097; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1520496097%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fsource%3Dsuggest%26q%3D%25E5%2589%258D%25E4%25BB%25BB%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=21a4461bbb469631.1516955420.7.1520496674.1520492685'
cookie = {}
for line in b.split(';'):
    key, value = line.split('=', 1)
    cookie[key] = value
print(cookie)

# requests.utils.dict_from_cookiejar()


'''
import requests,json
#引入requests和json模块。
session = requests.session()   
url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
data = {
'log': input('请输入你的账号:'),
'pwd': input('请输入你的密码:'),
'wp-submit': '登录',
'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-admin/',
'testcookie': '1'
}
session.post(url, headers=headers, data=data)

cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
#把cookies转化成字典。
print(cookies_dict)
#打印cookies_dict
cookies_str = json.dumps(cookies_dict)
#调用json模块的dumps函数，把cookies从字典再转成字符串。
print(cookies_str)
#打印cookies_str
f = open('cookies.txt', 'w')
#创建名为cookies.txt的文件，以写入模式写入内容。
f.write(cookies_str)
#把已经转成字符串的cookies写入文件。
f.close()
#关闭文件。
'''

# # 读取cookies的代码如下
# cookies_txt = open('cookies.txt', 'r')
# # 以reader读取模式，打开名为cookies.txt的文件。
# cookies_dict = json.loads(cookies_txt.read())
# # 调用json模块的loads函数，把字符串转成字典。
# cookies = requests.utils.cookiejar_from_dict(cookies_dict)
# # 把转成字典的cookies再转成cookies本来的格式。
# session.cookies = cookies
# # 获取cookies：就是调用requests对象（session）的cookies属性。


# 优化后代码
import requests, json

session = requests.session()
# 创建会话。
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
# 添加请求头，避免被反爬虫。
try:
    # 如果能读取到cookies文件，执行以下代码，跳过except的代码，不用登录就能发表评论。
    cookies_txt = open('cookies.txt', 'r')
    # 以reader读取模式，打开名为cookies.txt的文件。
    cookies_dict = json.loads(cookies_txt.read())
    # 调用json模块的loads函数，把字符串转成字典。
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    # 把转成字典的cookies再转成cookies本来的格式。
    session.cookies = cookies
# 获取cookies：就是调用requests对象（session）的cookies属性。

except FileNotFoundError:
    # 如果读取不到cookies文件，程序报“FileNotFoundError”（找不到文件）的错，则执行以下代码，重新登录获取cookies，再评论。

    url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    # 登录的网址。
    data = {'log': input('请输入你的账号:'),
            'pwd': input('请输入你的密码:'),
            'wp-submit': '登录',
            'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-admin/',
            'testcookie': '1'}
    # 登录的参数。
    session.post(url, headers=headers, data=data)
    # 在会话下，用post发起登录请求。

    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    # 把cookies转化成字典。
    cookies_str = json.dumps(cookies_dict)
    # 调用json模块的dump函数，把cookies从字典再转成字符串。
    f = open('cookies.txt', 'w')
    # 创建名为cookies.txt的文件，以写入模式写入内容
    f.write(cookies_str)
    # 把已经转成字符串的cookies写入文件
    f.close()
# 关闭文件

url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# 文章的网址。
data_1 = {
    'comment': input('请输入你想评论的内容：'),
    'submit': '发表评论',
    'comment_post_ID': '13',
    'comment_parent': '0'
}
# 评论的参数。
comment = session.post(url_1, headers=headers, data=data_1)
# 在创建的session下用post发起评论请求，放入参数：文章网址，请求头和评论参数，并赋值给comment。
print(comment.status_code)
# 打印comment的状态码
