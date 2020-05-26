# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

import requests

# headers = {
#     "origin": "https: // y.qq.com",
#     "referer": "https: // y.qq.com / portal / search.html",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
# }
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
}
client_url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp"
params = {
    "ct": "24",
    "qqmusic_ver": "1298",
    "new_json": "1",
    "remoteplace": "txt.yqq.song",
    "searchid": "62381926138386794",
    "t": "0",
    "aggr": "1",
    "cr": "1",
    "catZhida": "1",
    "lossless": "0",
    "flag_qc": "0",
    "p": "1",
    "n": "10",
    "w": "五月天",
    "g_tk": "490628805",
    "loginUin": "757585105",
    "hostUin": "0",
    "format": "json",
    "inCharset": "utf8",
    "outCharset": "utf-8",
    "notice": "0",
    "platform": "yqq.json",
    "needNewCode": "0",
}

response = requests.get(url=client_url, headers=headers, params=params)
print(response.status_code)
print(response.apparent_encoding)
json_response = response.json()
list_music = json_response['data']['song']['list']
for music in list_music:
    print(music['name'])
    print("所属专辑：" + music['album']['name'])
    print("歌曲时长：" + str(music['interval']) + "秒")
    # https: // y.qq.com / n / yqq / song / 001qvvgF38HVc4.html
    print("歌曲播放链接：https://y.qq.com/n/yqq/song/" + music['mid'] + ".html\n\n")
