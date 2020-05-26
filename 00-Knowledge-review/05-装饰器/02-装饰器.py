# coding = utf-8


# 定义函数：完成包裹数据
def makeBold(fn):
    def wrapped():
        print("这里执行的是makeBold")
        return "<b>" + fn() + "</b>"
    return wrapped

# 定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        print("这里执行的是makeItalic")
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold
def test1():
    return "hello world-1"

@makeItalic
def test2():
    return "hello world-2"

@makeBold
@makeItalic
def test3():
    return "hello world-3"

print(test1())
print("############分割线############")
print(test2())
print("############分割线############")
print(test3())