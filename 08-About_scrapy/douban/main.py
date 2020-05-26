# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

# 导入cmdline模块,可以实现控制终端命令行。
from scrapy import cmdline

# 用execute（）方法，输入运行scrapy的命令。
cmdline.execute(['scrapy', 'crawl', 'douban'])
