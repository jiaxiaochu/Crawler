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
# 示例1：*
# 需求：匹配出，一个字符串第一个字母为大小字符，后面都是小写字母并且这些小写字母可有可无
import re

# 需求：匹配出，一个字符串第一个字母为大小字符，后面都是小写字母并且这些小写字母可有可无
ret = re.match("[A-Z][a-z]*", "M")
print(ret.group())

ret = re.match("[A-Z][a-z]*", "MnnMrtyu")
print(ret.group())

ret = re.match("[A-Z][a-z]*", "Abcdefghi")
print(ret.group())

ret = re.match("[A-Z][a-z]*", "AbcdeFghi")
print(ret.group())

print("*" * 77)
ret = re.match("A.+", "AbcdeFghi")
print(ret.group())

