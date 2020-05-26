# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

'''
在正常的网页浏览过程中，如果发生速度很慢的情况，我们会做的选择是刷新页面，那么在代码中，我们是否也可以刷新请求呢？
对应的，retrying模块就可以帮助我们解决
retrying模块的地址：https://pypi.org/project/retrying/
retrying 模块的使用
使用retrying模块提供的retry模块
通过装饰器的方式使用，让被装饰的函数反复执行
retry中可以传入参数stop_max_attempt_number,让函数报错后继续重新执行，达到最大执行次数的上限，如果每次都报错，整个函数报错，如果中间有一个成功，程序继续往后执行
所以我们可以结合前面的知识点和retrying模块，把我们需要反复使用的请求方法做一个简单的封装，在后续任何其他地方需要使用的时候，调用该方法就行
'''

import requests
from retrying import retry

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}


@retry(stop_max_attempt_number=3)  # 最大重试3次，3次全部报错，才会报错
def _parse_url(url):
    response = requests.get(url, headers=headers, timeout=3)  # 超时的时候回报错并重试
    assert response.status_code == 200  # 状态码不是200，也会报错并充实
    return response


def parse_url(url):
    try:  # 进行异常捕获
        response = _parse_url(url)
    except Exception as e:
        print(e)
        response = None
    return response
