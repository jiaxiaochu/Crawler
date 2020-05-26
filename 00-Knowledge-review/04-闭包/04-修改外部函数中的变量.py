# coding = utf-8


def counter(start=0):
    def incr():
        nonlocal start
        # nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
        # nonlocal  适用于在局部函数 中 的局部函数，
        # 把最内层的局部 变量设置成外层局部可用，但是还不是全局的
        start += 1
        return start

    return incr


c1 = counter(5)
print(c1())
print(c1())

c2 = counter(50)
print(c2())
print(c2())

print(c1())
print(c1())

print(c2())
print(c2())

# def scope_test():
#     def do_local():
#         """
#         此函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。
#         此处的spam和外层的spam是两个变量，
#         如果写出spam = spam + “local spam” 会报错
#         :return:
#         """
#         spam = "local spam"
#
#     def do_nonlocal():
#         nonlocal spam       # 使用外层的spam
#         spam = "nonlocal spam"
#
#     def do_global():
#         global spam
#         spam = "global spam"
#     spam = "test spam"
#     do_local()
#     print("After do_local assignmane:", spam)
#     do_nonlocal()
#     print("After do_nonlocal assignment:", spam)
#     do_global()
#     print("After do_global assigment", spam)
#
# scope_test()
# print("In global scope:", spam)
