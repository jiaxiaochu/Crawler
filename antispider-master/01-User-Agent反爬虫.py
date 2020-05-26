# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
import requests
from parsel import Selector

url = "http://www.porters.vip/verify/uas/index.html"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safa"
}
resp = requests.get(url=url, headers=header)

if resp.status_code == 200:
    print("请求url:{} 成功".format(url))
    # print(resp.text)
    sel = Selector(resp.text)
    # 根据HTML标签和属性从响应正文中提取新闻标题
    res = sel.css('.list-group-item::text').extract()
    print(res)
else:
    print("请求url:{} 失败".format(url))
