# -*- coding:utf-8 -*-
"""
爬虫四大步骤：
    1.获取响应数据
    2.解析数据(响应数据)
    3.提取数据
    4.保存数据

程序的结构设计:
步骤1：获取响应数据,从网络上获取大学排名网页内容
              get_html()
步骤2：解析和提取数据,提取网页内容中信息到合适的数据结构
              parse_data()
步骤3：利用数据结构展示并输出结果
              print_data()
步骤4：只用csv文件存储数据
              print_data()
"""
# 导(引)入需要的爬虫库
import requests
import os
import csv
import openpyxl
import bs4
from bs4 import BeautifulSoup


def get_html(url):
    """定义获取网页源码函数"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
    }
    try:
        # 从目标url中提取文本信息
        response = requests.get(url, headers=headers, )  # timeout=20
        if response.status_code == 200:
            print("{} 请求成功".format(response.url))
            # 修改响应信息的字符编码
            response.encoding = response.apparent_encoding
            # 以文本的形式返回响应信息
            return response.text
        else:
            print("请求失败")
    except:
        return None


def parse_data(html, list):
    """定义从网页源码获取数据并处理数据函数"""
    # html.parser解释器可以将提取出的文本按标签进行分行，保证可读性
    soup = BeautifulSoup(html, 'html.parser')

    # 从源代码可以观察到，表格信息都是嵌套在tbody中，而每一行的信息由是嵌套在每一个tr标签中，每一行的每一格信息嵌套在td中，这也是html语言的特点。因此要遍历tbody中的每一个tr标签，即遍历每一行。
    for tr in soup.find('tbody').children:  # 返回一个上述列表的迭代器，也只有子节点
        # 为了防止文本字符中含有“tr"字段的信息被误认为html标签，因此需要进行标签确认
        if isinstance(tr, bs4.element.Tag):
            td = tr('td')
            # 提取出每一行表格前4列的信息
            t = [td[0].string, td[1].string, td[2].string, td[3].string]  # 把每个学校解析处的数据各自装到一个列表中
            list.append(t)  # 把每个学校信息列表都追加到一个大列表中，方便后面写入文件
            # return list  # 不能加return,造成的后果就是第一次循环时就把结果返回出去了，只取到了第一条数据


def print_data(ulist, num):
    """定义打印提取出表格信息的函数"""
    # 对输出结果进行format格式化输出，其中"{1:{3}^10}"中的{3}表示的是空余位置用format函数的第四个参数填充
    # {0:^10}中的:0是一个序号，表示格式化输出的第0个字符，依次累加；10表示输出宽度约束为10个字符；^表示输出时居中对齐，若宽度小于字符串的实际宽度，以实际宽度输出
    # 因为如果是按照默认的话，format中空余位置会用英文字符进行填充，这就造成了长短不一，输出不美观的影响
    # 而chr(12288)是中文空格对应的Unicode编码，这样就可以用中文空格填充空余位置了。

    # tplt = "{0:^10}\t{1:{5}^10}\t{2:^10}\t{:^10}"
    # tplt = "{:^10}\t{:^6}\t{:^10}\t{:^10}"
    # print(tplt.format("排名", "学校名称", "省份", "总分", chr(12288)))
    tplt = '{0:^9}\t\t{1:^9}\t\t{2:^10}\t{3:^9}'
    print(tplt.format('排名', '学校名称', '省市', '总分'))  # 表头的后两个元素的槽宽度进行调整才对齐
    title = tplt.format('排名', '学校名称', '省市', '总分')
    # rank = '{0:^9}'.format('排名')
    # school = '{1:^9}'.format('排名')
    # print(rank)
    # print("{0:^10}\t{1:{3}^10}\t{2:^10}".format('排名', '学校名称', '地区', '总分'))  # 表头的后两个元素的槽宽度进行调整才对齐
    for i in range(num):
        u = ulist[i]
        # print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))
        print('{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}'.format(u[0], u[1], u[2], u[3], chr(12288)))  # 中文空白字符


# def storing_data(list, num):  # num参数，控制提取多少组数据写入文件
#     """定义把数据写入文件函数"""
#     # for i in range(num):
#     #     u = list[i]
#     #     with open("./Universities_Ranking.csv", "a", encoding='utf-8')as file:
#     #         writer = csv.writer(file)
#     #         # writer.writerow(['排名', '学校', '分数'])
#     #         writer.writerow(u)
#
#     # 初始化函数 当类实例化时这个方法会自启动
#     wb = openpyxl.Workbook()
#     # 创建工作薄
#     ws = wb.active
#     # 定位活动表
#     ws.append(['排名', '学校名称', '省份', '总分'])
#     # 用append函数往表格添加表头
#     # line = [item['name'], item['author'], item['price']]
#     # 把图书名、作者和书的价格都写成列表的形式，赋值给line
#     ws.append(list)  # 用append函数把图书名、作者和书的价格等数据都添加进表格
#     wb.save('./Universities_Ranking2.csv')  # 保存文件
#     wb.close()  # 关闭文件


# def writercsv(save_road, num, title):
#     if os.path.isfile(save_road):
#         with open(save_road, 'a', newline='')as f:
#             csv_write = csv.writer(f, dialect='excel')
#             for i in range(num):
#                 u = list[i]
#                 csv_write.writerow(u)
#     else:
#         with open(save_road, 'a', newline='')as f:
#             csv_write = csv.writer(f, dialect='excel')
#             csv_write.writerow(title)
#             for i in range(num):
#                 u = list[i]
#                 csv_write.writerow(u)


def saveUnivData(uList):
    import csv
    with open('./Universities_Ranking2.csv', 'a') as file:
        writer = csv.writer(file)
        # 将列表的每条数据依次写入csv文件， 并以逗号分隔
        writer.writerows(uList)
        print("写入完成....")
    title = ["排名", "学校名称", "省市", "总分"]


def storing_data(title, num):  # num参数，控制提取多少组数据写入文件
    """定义把数据写入文件函数"""
    with open('./Universities_Ranking3.csv', 'a', newline='')as file:
        csv_write = csv.writer(file, dialect='excel')
        csv_write.writerow(title)
        for i in range(num):
            u = list[i]
            csv_write.writerow(u)


def main():
    list = []
    # year = input("请输入你想要爬取的学校排名的年份:")
    # start_url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming" + year + ".html"
    start_url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = get_html(start_url)
    parse_data(html, list)
    # 100代表爬取前100个学校
    print_data(list, 100)
    # 100代表将爬取的前100个学校存储进csv文件的数量
    # storing_data(list, 100)
    # saveUnivData(list)
    # title = ["排名", "学校名称", "省市", "总分"]
    # save_road = "./Universities_Ranking2.csv"
    # storing_data(title, 10)
    # writercsv(save_road, 10, title)


if __name__ == '__main__':
    main()
