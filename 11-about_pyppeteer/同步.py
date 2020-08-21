import time


def buy(what):
    print('购买商品{}'.format(what))
    time.sleep(1)
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print('获得商品{}，购买时间是：{}'.format(what, now_time))


buy('a')
buy('b')
buy('c')


