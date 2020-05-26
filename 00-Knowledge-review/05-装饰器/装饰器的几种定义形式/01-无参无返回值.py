# coding = utf-8


def outer1(func):
    def inner():
        print("装饰器语句1。。。")
        func()
        print("装饰语句2.。。")
    return inner    # 返回inner,实际上就是返回的inner内函数


# show1 = outer1(show1)
# 调用的是outer()函数
# 计算谁/执行谁，就把谁当参数传进去，
# 传进去之后，func接收

@outer1  # show = outer(show)
def show1():
    print("hello World")


if __name__ == '__main__':
    # 无参无返回值
    show1()