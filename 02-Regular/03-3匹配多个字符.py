# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
'''
字符	功能
*	匹配前一个字符出现0次或者无限次，即可有可无
+	匹配前一个字符出现1次或者无限次，即至少有1次
?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
{m}	匹配前一个字符出现m次
{m,n}	匹配前一个字符出现从m到n次

'''
# 需求：匹配出，0到99之间的数字
import re

ret = re.match("[1-9]", "73")
print(ret.group())
ret = re.match("[1-9][0-9]", "73")
print(ret.group())

ret = re.match("[1-9]*", "79678")
print(ret.group())

ret = re.match("[1-9]?\d*", "987654321")
print(ret.group())

ret = re.match("[1-9]?\d", "09")
print(ret.group())
