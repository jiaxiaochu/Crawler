# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
'''
字符	        功能
|	        匹配左右任意一个表达式
(ab)	    将括号中字符作为一个分组
\num	    引用分组num匹配到的字符串
(?P<name>)	分组起别名
(?P=name)	引用别名为name分组匹配到的字符串
'''
'''
字符	功能
*	匹配前一个字符出现0次或者无限次，即可有可无
+	匹配前一个字符出现1次或者无限次，即至少有1次
?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
{m}	匹配前一个字符出现m次
{m,n}	匹配前一个字符出现从m到n次

'''
# 示例1：|
# 需求：匹配出0-100之间的数字

import re

ret = re.match("[1-9]", "98")
print(ret.group())

ret = re.match("[1-9]?\d", "98")
print(ret.group())

# 不正确的情况
ret = re.match("[1-9]?\d", "98")
print(ret.group())

print("#" * 77)
# 修正之后
ret = re.match("[1-9]?\d$", "98")
# print(ret.group())
if ret:
    print(ret.group())
else:
    print("不在0-100之间")

print("#" * 77)
# 添加|
ret = re.match("[1-9]?\d$|100", "9")
print(ret.group())

ret = re.match("[1-9]?\d$|100", "98")
print(ret.group())

ret = re.match("[1-9]?\d$|100", "100")
print(ret.group())

ret = re.match("[1-9]?\d$|100", "09")   # 不是0-100之间
# print(ret.group())
