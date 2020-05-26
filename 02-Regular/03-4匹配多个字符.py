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

# 示例4：{m}
# 需求：匹配出，8到20位的密码，可以是大小写英文字母、数字、下划线
import re

ret = re.match("[a-zA-Z0-9_]{7}", "12a3g45678")
print(ret.group())

# 匹配出，8到20位的密码，可以是大小写英文字母、数字、下划线
ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")
print(ret.group())
