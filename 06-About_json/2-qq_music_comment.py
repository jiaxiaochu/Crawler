# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
}
request_url = "https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=490628805&loginUin=757585105&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=102065756&cmd=6&needmusiccrit=0&pagenum=1&pagesize=15&lasthotcommentid=song_102065756_34536033_1471101184&domain=qq.com&ct=24&cv=10101010"
response = requests.get(url=request_url, headers=headers)
print(response.status_code, '\n', response.apparent_encoding)
json_response = response.json()  # <class 'dict'>
list_comments = json_response['comment']['commentlist']
for comment in list_comments:
    print(comment['rootcommentcontent'])
    print("-" * 30)
