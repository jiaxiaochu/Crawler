# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
# coding=utf-8

'''
字符	功能
*	匹配前一个字符出现0次或者无限次，即可有可无
+	匹配前一个字符出现1次或者无限次，即至少有1次
?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
{m}	匹配前一个字符出现m次
{m,n}	匹配前一个字符出现从m到n次


'''
# 示例2：+
# 需求：匹配出，变量名是否有效
import re

names = ["name1", "_name", "2_name", "__name__"]

for name in names:
    ret = re.match("[a-zA-Z_]+[\w]*", name)
    # if ret:
    #     print("变量名 %s 符合要求" % ret.group())
    # else:
    #     print("变量名 %s 非法" % name)

data = re.match("[a-zA-Z_]+[\w]*", "name134")
print(data.group())

data = re.match("[a-zA-Z_]+[\d]", "Name134")
print(data.group())

data = re.match("[a-zA-Z_]+[\d]", "name134")
print(data.group())

data = re.match("[a-zA-Z_]+[\d]+", "name134")
print(data.group())
