# coding = utf-8


#### 第一波 ####
# def foo():
#     print("foo")
# foo     # 表示是函数
# foo()   # 表示只想foo函数


#### 第二波 ####
# def foo():
#     print("foo")
#
# foo = lambda x:x + 1
# foo()
# 执行lambda表达式，而不再是原来的foo函数，
# 因为foo这个名字被重新指向了另外一个匿名函数


def func():
    # print("hello world")
    return 'hahaha'


print(func())