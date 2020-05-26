# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
# import requests
# from lxml import etree
#
# url = "http://www.porters.vip/verify/cookie/content.html"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safa",
#     'Cookie': "isfirst=789kq7uc1pp4c"
# }
# resp = requests.get(url, headers=headers)
# if resp.status_code == 200:
#     print("请求url:{} 成功".format(url))
#     # print(resp.text)
#     html = etree.HTML(resp.text)
#     res = html.cssselect('.page-header h1')[0].text
#     print(res)
#
# else:
#     print("请求url:{} 失败".format(url))

import requests
from lxml import etree

url = "http://www.porters.vip/verify/cookie/content.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safa",
    'Cookie': "isfirst=789kq7uc1pp4c"
}
resp = requests.get(url, headers=headers)
if resp.status_code == 200:
    print("请求url:{} 成功".format(url))
    # print(resp.text)
    html = etree.HTML(resp.text)
    res = html.cssselect('.page-header h1')
    title_1 = res[0].text
    title_1_small = html.cssselect('.page-header h1 small')[0].text
    # print(title_1_small)
    author = html.cssselect('.page-header p')[0].text
    guide = html.cssselect('.left col-md-10')#[0].text
    print(guide)
else:
    print("请求url:{} 失败".format(url))
