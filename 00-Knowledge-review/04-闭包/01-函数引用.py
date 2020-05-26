# coding = utf-8


def func1():
    print("——这是函数一——")


func1()     # 调用函数
ret = func1     # 引用函数
print(id(ret))
print(id(func1))    # 引用的函数id一样
ret()


