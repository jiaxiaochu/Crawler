# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-

# https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20
# https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0
# https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20
# https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=40
# 构造url的思路：
# "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start="

# for page_num in range(0,3):
#     # print(page_num * 20,type(page_num * 20))   # <class 'int'>
#     print("https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=" + str(page_num * 20)
# )

import requests

# start_url = "https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"
s_url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

for page_num in range(0, 3):
    # print(page_num * 20,type(page_num * 20))   # <class 'int'>
    start_url = "https://movie.douban.com/j/search_subjects?"
    # print(start_url)
    params = {
        "type": "movie",
        "tag": "热门",
        "sort": "recommend",
        "page_limit": "20",
        "page_start": str(page_num * 20),
    }
    response = requests.get(url=start_url, headers=headers, params=params)
    print(response.url)
    # print(response.status_code)
    try:
        if response.status_code == 200:
            json_movie = response.json()
            # print(json_movie)
            list_movie = json_movie['subjects']
            # print(list_movie)
            for movie in list_movie:
                print(movie["title"])
        else:
            print("请求失败")
    except Exception as error:
        print(error)
