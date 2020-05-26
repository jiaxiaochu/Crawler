# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
# search
# 需求：匹配出文章阅读的次数
import re

ret = re.search(r"\d+", "阅读次数为 9999")
print(ret.group())
