# # coding = utf-8
#
#
#
#
#
# def outer(func):
#     def inner():
#         result = func()
#         print(next(result))
#         print(next(result))

#     return inner
#
#
# @outer  # count_num = outer(count_num)
# def count_num():
#     # str1 = 'hello'
#     for i in range(1, 5):
#         yield i
#
# count_num()


# result = count_num()
# print(next(result))
# print(next(result))


def func():
    # print('hello')
    return 'hahaha'
# func()
print(func())