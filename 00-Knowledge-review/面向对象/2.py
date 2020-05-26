# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-

class Animal(object):
    def __init__(self, name):
        self.name = name    # 属性

    def eat(self):      # 方法
        print("%s 吃 " % self.name)

    def drink(self):    # 方法
        print("%s 喝 " % self.name)

    def run(self):      # 方法
        print("%s 跑 " % self.name)


class Cat(Animal):

    def cry(self):       # 方法
        print("%s 喵喵叫" % self.name)


class Dog(Animal):

    def cry(self):       # 方法
        print("%s 汪汪叫" % self.name)


animal = Cat("小黑家的小白猫")    # 实例化
animal.eat()
animal.cry()
animal.run()
#
animal_2 = Dog("小白家的小黑狗")
animal_2.drink()
animal_2.cry()

# def __init__(self, name, color):
#     super().__init__(name, color)  # 颜色
#     # self.color = color  # 属性
#     self.tail = True  # 尾巴
