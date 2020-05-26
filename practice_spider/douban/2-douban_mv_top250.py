# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

'''
豆瓣Top250数据全部爬取
页面分析：
    第1页：https://movie.douban.com/top250?start=0&filter=
    第3页：https://movie.douban.com/top250?start=50&filter=
    第7页：https://movie.douban.com/top250?start=150&filter=
    发现只有start后面是有变化的，规律就是第N页，start=(N-1)*25
'''

import re
import openpyxl
import requests
from bs4 import BeautifulSoup


# 获取相应数据
def get_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        # response.status_code()
        response.raise_for_status()  # 如果返回的状态码不是200（请求不成功），则抛出异常
        response.encoding = response.apparent_encoding  # 根据响应判断网页的编码格式，便于response.text知道如何编码
    except Exception as e:
        print("爬取错误")
    else:
        print("爬取成功")
        return response.text


# 解析响应数据
def parser_content(html_content):
    '''
    实例化soup对象
    解析标签
    获取电影信息
        电影序号
        电影名称
        电影推荐语
        电影评分
        评价人数
        电影链接
    :param content:
    :return:
    '''
    soup = BeautifulSoup(html_content, 'html.parser')
    data = soup.find_all('div', class_="item")
    for item in data:
        num = item.find('em', class_="").text
        move_name = item.find('span', class_="title").text
        recommend = item.find('span', class_="inq")
        score = item.find('span', class_="rating_num").text
        score_people_count = item.find('span').text
        link = item.find('a')['href']
        if recommend:
            mv_recommend = recommend.text
        else:
            mv_recommend = '无短评'
        mv_info.append((num, move_name, mv_recommend, score, score_people_count, link))
        # print(num.text + move_name + recommend + score + link)


# 持久化存储（保存到excel文件）
def save_to_excel(file_name, data, sheetname):
    print("正在创建excel表格%s......" % (file_name))
    # 使用openpyxl实例化一个workbook对象
    wb = openpyxl.Workbook()
    # 获取当前活动表格对象
    sheet = wb.active
    # 将数据写入excel表格中
    sheet.title = sheetname
    print("......正在写入数据............")
    for row, detail in enumerate(data):
        for column, cellvalue in enumerate(detail):
            cell = sheet.cell(row=row + 1, column=column + 1, value=cellvalue)
    wb.save(file_name)
    print("亲，让你久等了，保存工作簿%s成功......" % (file_name))


if __name__ == '__main__':
    doubanTopPage = 10
    perPage = 25
    mv_info = []
    for page in range(1, doubanTopPage + 1):
        url = 'https://movie.douban.com/top250?start=0&filter=%s' % ((page - 1) * perPage)
        content = get_content(url)
        parser_content(content)
    save_to_excel('../../source/source_file/douban_mv.xlsx', mv_info, sheetname='豆瓣Top250电影信息')
