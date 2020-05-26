# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
# urls = ["http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-%d" % i for i in range(1, 26)]
# print(urls)

# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
import time
import requests
import asyncio, aiohttp


# 获取网页(文本信息)
async def get_content(session, url):
    async with session.get(url) as response:
        return await response.text(encoding='gb18030')


# 解析网页
def parser_content(html):
    print(html)


# 处理网页
async def download(url):
    async with aiohttp.ClientSession() as session:
        html = await get_content(session, url)
        parser_content(html)



# 全部网页
urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-%d' % i for i in range(1, 3)]

# 统计该爬虫的消耗时间
print('#' * 50)
t1 = time.time()  # 开始时间

# 利用asyncio模块进行异步IO处理
'''
获取Eventloop
执行coroutine
'''
loop = asyncio.get_event_loop()
# loop.run_until_complete(download(urls))
tasks = [asyncio.ensure_future(download(url)) for url in urls]
tasks = asyncio.gather(*tasks)
loop.run_until_complete(tasks)
loop.close()

t2 = time.time()  # 结束时间
print('使用一般方法，总共耗时：%s' % (t2 - t1))
print('#' * 50)
