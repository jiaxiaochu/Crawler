# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

import csv

with open("demo.csv", "w", encoding='utf-8')as file:
    writer = csv.writer(file)
    writer.writerow(['电影', '豆瓣评分'])
    writer.writerow(['银河护卫队', '8.0'])
    writer.writerow(['复仇者联盟', '8.1'])

"""
import csv

# 需要写入的数据
score1 = ['math', 95]
score2 = ['english', 90]

# 打开文件，追加a, newline=""，可以删掉行与行之间的空格
file= open("score.csv", "a", newline="")

# 设定写入模式
csv_write = csv.writer(file)

# 写入具体内容
csv_write.writerow(score1)
csv_write.writerow(score2)
file.close()
"""
