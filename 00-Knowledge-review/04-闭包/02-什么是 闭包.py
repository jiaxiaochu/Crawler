# coding = utf-8


# 定义一个函数
def func1(number):
    # 在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，
    # 那么将这个函数以及用到的一些变量称之为闭包
    def func2(number_in):
        print("in func2 函数, numbe_in is %d" % number_in)
        return number + number_in

    return func2


# 给func1函数赋值，这个20是给参数number
ret = func1(20)
print(ret(100))  # 注意：这里的100是给参数number_in
print(ret(200))  # 注意：这的200是给参数number_in
