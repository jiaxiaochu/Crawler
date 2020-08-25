import time
import asyncio


async def buy(what):
    print('购买商品{}'.format(what))
    await asyncio.sleep(1)
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print('获得商品{}，购买时间是：{}'.format(what, now_time))


async def main():
    await asyncio.gather(buy('a'), buy('b'), buy('c'))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()



