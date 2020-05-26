# coding = utf-8


def outer2(func):
    def inner(string):
        print("装饰器语句1。。。")
        func(string)
        print("装饰语句2.。。")
    return inner    # 返回inner,实际上就是返回的inner内函数


@outer2  # show2 = outer2(show2)
def show2(string):
    print("hello  " + string)


if __name__ == '__main__':
    # 有参无返回值
    show2("Python")