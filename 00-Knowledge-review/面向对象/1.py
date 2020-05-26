# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
class Animal(object):
    def __init__(self, color):
        self.color = color  # 属性

    def call(self):  # 方法
        print("动物叫。。。")


class Fish(Animal):
    def __init__(self, color):
        super().__init__(color)  # 颜色
        # self.color = color  # 属性
        self.tail = True  # 尾巴

    def call(self):
        print("%s的鱼在吐泡泡" % self.color)


fish = Fish("蓝色")
fish.call()
# animal = Animal("白色")
# animal.call()
