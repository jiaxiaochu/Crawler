# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
# 提取区号和电话号码
import re

# ret = re.match("([^-]+)-\d{8}", "010-12345678")
ret = re.match("([^-]+)-\d+", "010-12345678")
print(ret.group())

