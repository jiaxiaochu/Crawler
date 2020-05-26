# coding = utf-8


def add_b():
    global b
    b = 42
    print("This id add_b's", b)

    def do_global():
        global b
        b = b + 10
        print("This is do_global's", b)

    do_global()
    print(b)


add_b()
# global 定义的变量，表明其作用域在局部以外，
# 即局部函数执行完之后，不销毁 函数内部以global定义的变量

# def add_b():
#     global  b
#     b = 42
#     def do_global():
#         global  a
#         a = b + 10
#         print(b)
#     do_global()
#     print(a)
# add_b()
# print("a = %s , b = %s " %(a, b))

# def add_b():
#     #global  b
#     b = 42
#     def do_global():
#         global  b
#         b =  10
#         print(b)
#     do_global()
#     print(b)
# add_b()
# print(" b = %s " % b)
