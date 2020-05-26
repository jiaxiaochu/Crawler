# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-


# 匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com

import re

email_accpunt = "hello@163.com"
data = re.match("[a-zA-Z]", email_accpunt)
print(data.group())

'''
zhangsan-001@gmail.com 
分析邮件名称部分：
    26个大小写英文字母表示为a-zA-Z
    数字表示为0-9
    下划线表示为_
    中划线表示为-
    由于名称是由若干个字母、数字、下划线和中划线组成，所以需要用到+表示多次出现
'''
#  根据以上条件得出邮件名称表达式：[a-zA-Z0-9_-]+
email_accpunt = "zhangsan-001@gmail.com"
data = re.match("[a-zA-Z0-9_-]+", email_accpunt)
print(data.group())
'''
分析域名部分：
    一般域名的规律为“[N级域名][三级域名.]二级域名.顶级域名”，比如“qq.com”、“www.qq.com”、“mp.weixin.qq.com”、“12-34.com.cn”，分析可得域名类似“** .** .** .**”组成。
    “**”部分可以表示为[a-zA-Z0-9_-]+
    “.**”部分可以表示为\.[a-zA-Z0-9_-]+
    多个“.**”可以表示为(\.[a-zA-Z0-9_-]+)+
'''
# 综上所述，域名部分可以表示为[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+
# 由于邮箱的基本格式为“名称@域名”，需要使用“^”匹配邮箱的开始部分，用“$”匹配邮箱结束部分以保证邮箱前后不能有其他字符，所以最终邮箱的正则表达式为：
data = re.match("^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-z0-9]{2,})$", "zhangsan-001@gmail.com")
print(data.group())

# "^[a-z0-9A-Z]+[- | a-z0-9A-Z . _]+@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?\\.)+[a-z]{2,}$"
data = re.match("^[a-z0-9A-Z]+[- | a-zA-Z0-9 . _]+@([a-zA-Z0-9]+(-[a-zA-Z0-9]+)?\\.)+[a-z]{3}$",
                "zhangsan-001@gmail.com")
print(data.group())

'''
字符	功能
*	匹配前一个字符出现0次或者无限次，即可有可无
+	匹配前一个字符出现1次或者无限次，即至少有1次
?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
{m}	匹配前一个字符出现m次
{m,n}	匹配前一个字符出现从m到n次
'''
