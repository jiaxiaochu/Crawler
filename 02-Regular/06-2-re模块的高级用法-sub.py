# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
# sub 将匹配到的数据进行替换
# 需求：将匹配到的阅读次数加1
import re

# 方法1：
ret = re.sub(r"\d+", "999", "python = 997")
print(ret)

# 方法2：
import re


def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


ret = re.sub(r"\d+", add, "python = 997")
print(ret)

ret = re.sub(r"\d+", add, "python = 99")
print(ret)
