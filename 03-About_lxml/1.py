# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
"""
导入lxml 的 etree 库 (导入没有提示不代表不能用)

 `from lxml import etree`
利用etree.HTML，将字符串转化为Element对象,Element对象具有xpath的方法,返回结果的列表，能够接受bytes类型的数据和str类型的数据

html = etree.HTML(text)
ret_list = html.xpath("xpath字符串").decode()
把转化后的element对象转化为字符串，返回bytes类型结果 etree.tostring(element)
"""

from lxml import etree

text = ''' <div> <ul> 
        <li class="item-1"><a>first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a> 
        </ul> </div> '''

# 根据li标签进行分组
html = etree.HTML(text)

#获取href的列表和title的列表
# href_list = html.xpath("//li[@class='item-1']/a/@href")
# title_list = html.xpath("//li[@class='item-1']/a/text()")


li_list = html.xpath("//li[@class='item-1']")
# print(li_list)
# #
item = {}
for li in li_list:
    item["href"] = li.xpath("./a/@href")[0] if len(li.xpath("./a/@href")) > 0 else None
    item["title"] = li.xpath("./a/text()")[0] if len(li.xpath("./a/text()")) > 0 else None
    print(item)
