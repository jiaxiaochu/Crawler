# coding = utf-8


def outer(func):
    def inner(*args, **kwargs): # 接收不同的参数
        print("装饰语句1。。。")
        result = func(*args, **kwargs)
        print("装饰语句2。。。")
        return result   # 再原样传回给被装饰的函数
    return inner    # 返回inner,实际上就是返回的inner内函数


@outer  # show = outer(show)
def show(string, m, n):
    return "hello  " + string + str(m) + str(n)


if __name__ == '__main__':
    # 有参无返回值
    print(show("world  ", 100, "    hahaha"))

"""
温故而知新：
不定长参数有两种：*args 和**kwargs;
*args：是不定长参数，用来将参数打包成 tuple 给函数体调用
**kwargs:是关键字参数，打包关键字参数成 dict 给函数体调用
在定义函数的时候不确定要传入的参数个数会有多少个的时候就可以使用不定长参数作为形参
"""