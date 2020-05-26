# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-


import requests
from bs4 import BeautifulSoup

post_url = 'https://xiaoke.kaikeba.com/example/wordpress/2019/11/07/互联网圈炸锅啦！有人要帮你加薪啦！/'
url_login = 'https://xiaoke.kaikeba.com/example/wordpress/wp-login.php?action=postpass'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

session = requests.session()


def getContent():
    res = session.get(post_url, headers=headers)
    html_content = BeautifulSoup(res.text, 'html.parser')
    post_content = html_content.find('div', class_='entry-content')
    if (post_content is None):
        print('没有内容')
    else:
        print(post_content.text)


getContent()

data_login = {
    'post_password': 'xiaoke123',
    'Submit': '提交'
}
res = session.post(url_login, headers=headers, data=data_login)
print(res.status_code)

getContent()
