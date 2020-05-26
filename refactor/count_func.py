from time import ctime, sleep


def count_time(func):
    def wrapped_func():
        print("%s called at %s" % (func.__name__, ctime()))
        func()

    return wrapped_func


@count_time
def foo():
    print("I am foo")


foo()
sleep(2)
foo()
