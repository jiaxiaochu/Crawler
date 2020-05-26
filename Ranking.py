# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
import re
import requests
import bs4


def fetchUrl(url):
    '''
    功能：根据参数 url ，发起 http request，尝试获取指定网页并返回结果
    参数：
            url：某个 webpage 的url
    返回：类文件对象型 http Response 对象
    '''
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('success!')
        return r.text
    except requests.RequestError as e:
        print(e)
    except:
        return "Error!"


def parserHtml(html, urating):
    '''
    功能：根据参数 html 给定的内存型 HTML 文件，尝试解析其结构，获取所需内容
    参数：
            html：类似文件的内存 HTML 文本对象
            urating：一个二维列表，存放着大学排名信息
    返回：一个二维列表，存放着大学排名信息
    '''
    bsobj = bs4.BeautifulSoup(html, 'html.parser')

    # 获取表头信息
    tr = bsobj.find('thead').find('tr')
    hlist = []

    if isinstance(tr, bs4.element.Tag):
        for th in tr('th'):
            hlist.append(th.string)
        hlist.pop()
        for option in tr('option'):
            hlist.append(option.string)
        urating.append(hlist)

    # 获取表体信息
    for tr in bsobj.find('tbody').children:
        blist = []
        if isinstance(tr, bs4.element.Tag):
            for td in tr('td'):
                blist.append(td.string)
            urating.append(blist)

    return urating


def output(urating, filename):
    '''
    功能：格式化输出结果
    参数：
            urating：存放着排名结果的二维列表
            filename：保存的文件名
    返回：无
    '''
    import pandas as pd
    dataframe = pd.DataFrame(urating)
    dataframe.to_csv(filename, index=False, sep=',', header=False)

    print("Success!")


def main():
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'

    print(
        "Begin to crawl the http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html and get the rating of universities in china ...")
    print('---' * 20)
    print("Try to fetch url ...")
    html = fetchUrl(url)

    print("Try to parser html ...")
    urating = []
    ur = parserHtml(html, urating)

    print("Try to save the results in file ...")
    output(ur, '大学排名2018.csv')

    print("The work of crawling is done.")


if __name__ == '__main__':
    main()
