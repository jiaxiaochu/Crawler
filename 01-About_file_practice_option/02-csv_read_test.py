# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
# @Time : 2019/12/11


'''
import csv

with open("../source/source_file/demo.xlsx", "w", encoding='utf-8')as file:
    writer = csv.writer(file)
    writer.writerow(['电影', '豆瓣评分'])
    writer.writerow(['银河护卫队', '8.0'])
    writer.writerow(['复仇者联盟', '8.1'])
'''

import csv

with open("../source/source_file/demo.xlsx", "r", encoding='utf-8')as file:
    reader = csv.reader(file)
    print(reader)
    for content in reader:
        print(content)


"""
import csv

# 打开csv文件
file = open("score.csv")

# 读取文件内容，构造csv.reader对象
reader = csv.reader(file)

# 打印reader中的内容
for item in reader:
    print(item)
file.close()
"""
