# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang


# 小说楼：https://www.xslou.com/
# 小说楼登录：https://www.xslou.com/login.php
# 小说楼的排行榜：https://www.xslou.com/top/allvisit_1/
# 小说楼催更：https://www.xslou.com/modules/article/usercui.php?id=

# 使用Python登录小说楼，爬取热榜小说，对作者进行催更。
# 模拟登录获取cookies
# 拿到书籍的id
# 使用id参数和cookies请求催更


import requests

# 创建回话
session = requests.session()
# 准备数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
login_url = 'https://www.xslou.com/login.php'  # 登录连接
hot_url = 'https://www.xslou.com/top/allvisit_1/'  # 排行榜连接
urge_url = 'https://www.xslou.com/modules/article/usercui.php?id='  #


