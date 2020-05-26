# coding = utf-8
import time


def count_number():
    s = 0
    for i in range(5):
        s += i
    print(s)


def count_time(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return inner    # 返回inner,实际上就是返回的inner内函数

count_number = count_time(count_number)
count_number()

# 1.调用的是count_time()计算时间的函数
# 2.计算谁/执行谁==count_number，就把谁(count_number)当参数传进去
# 3.传进去之后，func接收
###########################################
# 4.count_time函数返回的是什么？
# count_time函数返回的是inner内部函数
###########################################
# 5.也就是说，一但执行完count_time函数调用之后,
# count_number = count_time(count_number)的count_number指向的是count_time中的inner
# 当一但执行count_number的时候，实际上执行的是inner函数，相应的也就把时间计算出来啦
# 也就能执行原来count_number的函数功能