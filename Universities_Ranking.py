import csv
import os
import requests
import pandas
from bs4 import BeautifulSoup

all_Universities = []


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""


def fillUnivList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        # print(ltd)
        if len(ltd) == 0:
            continue
        # singleUniv = []
        info_list = []
        for td in ltd:
            # print(td.string)
            data = td.string
            info_list.append(data)
        print(info_list[0], info_list[1], info_list[2], info_list[3])
        # singleUniv.append(td.string)
        # allUniv.append(singleUniv)
        # print(singleUniv[0], singleUniv[1], singleUniv[2], singleUniv[3])


def storing_data(title, num):  # num参数，控制提取多少组数据写入文件
    """定义把数据写入文件函数"""
    with open('./Universities_Ranking3.csv', 'a', newline='')as file:
        csv_write = csv.writer(file, dialect='excel')
        csv_write.writerow(title)
        for i in range(num):
            u = all_Universities[i]
            csv_write.writerow(u)


def writercsv(save_road, num, title):
    if os.path.isfile(save_road):
        with open(save_road, 'a', newline='')as f:
            csv_write = csv.writer(f, dialect='excel')
            for i in range(num):
                u = all_Universities[i]
                csv_write.writerow(u)
    else:
        with open(save_road, 'w', newline='')as f:
            csv_write = csv.writer(f, dialect='excel')
            csv_write.writerow(title)
            for i in range(num):
                u = all_Universities[i]
                csv_write.writerow(u)


def main():
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    fillUnivList(soup)
    title = ["排名", "学校名称", "省市", "总分"]
    # save_road = "./Universities_Ranking3.csv"
    # writercsv(save_road, 10, title)
    storing_data(title, 100)


if __name__ == '__main__':
    main()
