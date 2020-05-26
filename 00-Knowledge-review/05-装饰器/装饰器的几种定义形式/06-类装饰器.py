# coding =- utf-8
# import time


# class Wrapper(object):
#     def __init__(self, func):
#         self.__func = func
#
#     def __call__(self, *args, **kwargs):
#         print("装饰语句1。。。")
#         result = self.__func(*args, **kwargs)
#         print("装饰语句2。。。")
#         result result
import time

class Wrapper(object):
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.__func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return result


@Wrapper
def show(): # 无参无返回值
    print("hello world")

#
# @Wrapper
# def show1(string):  # 有参无返回值
#     print("hello    " + string)
#
#
# @Wrapper
# def show2():    # 无参有返回值
#     return "hello world"
#
#
# @Wrapper
# def show3(string, m):   # 有参有返回值
#     return "hello  " + string + str(m)


@Wrapper
def show4(string, m, n):    # 有参有返回值
    return "hello  " + string + str(m) + str(n)

if __name__ == '__main__':
    show()    # 无参无返回值
    # show1("world")    # 有参无返回值
    # print(show2())    # 无参有返回值
    # print(show3("python   ", 100))    # 有参有返回值
    # print(show4("Go ", "C++ ", 1000))     # 有参有返回值
