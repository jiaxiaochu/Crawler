# coding = utf-8


def outer4(func):
    def inner(string, m):
        print("装饰语句1。。。")
        result = func(string, m)
        print("装饰语句2。。。")
        return result
    return inner    # 返回inner,实际上就是返回的inner内函数


@outer4  # show4 = outer4(show4)
def show4(string, m):
    return "hello  " + string + str(m)


if __name__ == '__main__':
    # 有参无返回值
    print(show4("world  ", 100))