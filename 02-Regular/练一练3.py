# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
# 不是以4、7结尾的手机号码(11位)
import re

tels = ["13100001234", "18912344321", "10086", "18800007777"]
for tel in tels:
    # ret = re.match("^1\d{10}", tel)
    ret = re.match("^1\d{9}[0-35-68-9]", tel)  # 不是以4、7结尾的手机号码(11位)
    if ret:
        print(ret.group())
    else:
        print("{}不是想要的手机号".format(tel))
