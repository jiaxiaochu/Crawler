# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-

# 请提取url地址

import re

str = '''
<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" 
src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" 
style="display: inline;">
'''
ret = re.search(r"https://.*?\.jpg", str)
print(ret.group())
