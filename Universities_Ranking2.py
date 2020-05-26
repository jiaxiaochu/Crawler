# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
# 引入需要的库
import requests
from bs4 import BeautifulSoup
import bs4

# 准备请求数据
start_url = "http://zuihaodaxue.cn/zuihaodaxuepaiming2019.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
}
response = requests.get(url=start_url, headers=headers)
if response.status_code == 200:
    # print("请求成功")
    # print(response.text)
    # 修改响应信息的字符编码
    response.encoding = response.apparent_encoding
    # 将获取到的响应信息以文本的形式通过'html.parser'做格式化操作
    soup = BeautifulSoup(response.text, 'html.parser')
    # datas = html.find('div', class_="news-text").text
    # datas = soup.find('tbody', class_="hidden_zhpm")
    datas = soup.find('tr').children
    # print(datas)
    for tr in datas:
        if isinstance(tr, bs4.element.Tag):
            td_data = tr('td')
            print(td_data)
#     for data in datas:
#         school_name = data.find('tbody', class_="hidden_zhpm")
#         print(school_name)
else:
    print("请求失败")
