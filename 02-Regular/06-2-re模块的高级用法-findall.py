# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
# findall
# 需求：统计出python、c、c++相应文章阅读的次数

import re

ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
# 默认返回列表
print(ret)  # ['9999', '7890', '12345']
