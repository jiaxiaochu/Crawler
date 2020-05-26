# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
# 需求：匹配出163、126、qq邮箱

import re

ret = re.match("\w{4,20}@163\.com", "test@163.com")
print(ret.group())

ret = re.match("\w+@\d+\.[a-z]{3}$", "test@163.com")
print(ret.group())

# ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@qq.com")
ret = re.match("^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]{3}$", "test@qq.com")
print(ret.group())
