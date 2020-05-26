# coding = utf-8


def outer3(func):
    def inner():
        print("装饰语句1。。。")
        result = func()
        print("装饰语句2。。。")
        return result
    return inner    # 返回inner,实际上就是返回的inner内函数


@outer3  # show3 = outer3(show3) b
def show3():
    return "hello  world"


if __name__ == '__main__':
    # 有参无返回值
    print(show3())