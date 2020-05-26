# coding = utf-8



# import time
#
#
# def count_time(func):
#     def inner():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         return end_time - start_time
#         # print(end_time - start_time)
#     return inner  # 返回inner,实际上就是返回的inner内函数
#
#
# @count_time   # count_num = count_time(count_num)
# def count_num():
#     numb = 0
#     for i in range(101):
#         numb += i
#     print(numb)
#
# count_num = count_time(count_num)
# print(count_num())



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

@Wrapper
def show4(string, m, n):    # 有参有返回值
    return "hello  " + string + str(m) + str(n)

if __name__ == '__main__':
    # show()    # 无参无返回值
    # show1("world")    # 有参无返回值
    # print(show2())    # 无参有返回值
    # print(show3("python   ", 100))    # 有参有返回值
    print(show4("Go ", "C++ ", 1000))     # 有参有返回值