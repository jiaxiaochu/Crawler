# coding = utf-8
"""
装饰器原理
使用装饰器的条件：
1.不能修改被装饰的函数的源代码
2.不能

"""
import time


def count_time(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print(end - start)

    return inner  # 返回inner,实际上就是返回的inner内函数


@count_time  # count_number = count_time(count_number)
def count_number():  # 被装饰后，count_number()指向inner()
    s = 0
    for i in range(5):
        s += i
    print(s)


# count_number = count_time(count_number)
if __name__ == '__main__':
    count_number()
"""
# 从程序运行的结果来看，是先执行了count_number()函数中的累加。
# 然后输出了结束时间减去开始时间的结果。 
# 可是我明明只调用了count_number()函数，为什么最终程序执行的结果出来了该函数以外的东西？ 
# 那是由于在count_number函数在声明的过程中，被装饰器@count_time所装饰了。
# 因此在程序最终的执行过程中，出现了除了count_number()之外的结果。
# 简单的来说，这也就是装饰器的作用。 
# 在执行程序A的时候顺便执行程序B。
# 但也不仅仅于此。下面，我们来具体剖析一下这段程序，
# 以了解和熟悉装饰器以及为何不仅仅于“在执行程序A的时候顺便执行程序B”，
# 当然，这也是装饰器的最大的意义，以及其与闭包等的区别。
"""

# 1.执行count_number()——>>先调用count_time()计算时间的函数
# 2.计算谁/执行谁==count_number，就把谁(count_number)当参数传进去(传给调用函数count_time)
# 3.传进去之后，func接收
###########################################
# 4.count_time函数返回的是什么？
# count_time函数返回的是inner内部函数
###########################################
# 5.也就是说，一但执行完count_time函数调用之后,count_number = count_time(count_number)的count_number指向的是count_time中的inner
# 当一但执行count_number的时候，实际上执行的是inner函数，代码从上往下执行，相应的也就把时间计算出来啦
# 也就能执行原来count_number的函数功能

# 装饰器装饰过程：在执行@xxx时候，实际就是将原函数(被装饰函数)传递到闭包中，然后原函数的引用指向闭包返回的装饰过的内部函数的引用
# func = wrapper(func) func是被装饰函数，wrapper是装饰器

"""
@count_time  #counter_number = count_time(count_number)
一旦这个函数被装饰器所装饰，那么这个函数就不在指向原函数对象,而是指向了装饰器(count_time)返回的函数对象(inner)
counter_number = count_time(count_number)
指向inner为什么原来的函数能执行？
是因为count_time(func)中func接收，func去执行
"""
