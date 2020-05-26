# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
url = 'https://www.zhihu.com/api/v4/members/lisanshui1230/articles'
list_article = []
# 建立一个空列表，以待写入数据
offset = 0
# 设置offset的起始值为0
while True:
    params = {
        'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset': str(offset),
        'limit': '20',
        'sort_by': 'created',
    }
    # 封装参数
    res = requests.get(url, headers=headers, params=params)
    # 发送请求，并把响应内容赋值到变量res里面
    articles = res.json()
    # print(articles)
    data = articles['data']
    # 定位数据
    for i in data:
        article_info = [i['title'], i['url'], i['excerpt']]
        # 把数据封装成列表
        print(article_info)
        # 打印看看
    offset = offset + 20
    # 在while循环内部，offset的值每次增加20
    if offset >= 60:
        break
    # 如果offset大于等于60，即爬了3页，就停止
