import requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4
import csv
import os


# 获取页面数据
def get_html_text(url):
    r = requests.get(url)
    if r.status_code == 200:
        print('爬取成功')
        r.encoding = 'UTF-8'
        return r.text
    else:
        print('爬取失败')


# 获取老师信息，并保存
def get_teachers_info(html, ilt):
    soup = BeautifulSoup(html, 'html.parser')
    # 找到基本信息
    people = soup.find_all('article')
    for person in people:
        name = person.find('span').get_text()
        feature = person.find('strong').get_text().strip()
        introduction = person.find('div', attrs={'class': 'mc-description'}).get_text().strip().replace(' ', '')
        img = person.find('img').get('src')
        url_img = 'http://show.ybccode.com/teachers/' + img
        ilt.append([name, feature, introduction, url_img])


# 下载页面上的图片
def get_teachers_img(ilt):
    # 新建images文件夹
    path = 'images/'
    if not os.path.exists(path):
        os.mkdir(path)

    # 依次下载每个老师的图片
    for lt in ilt:
        name = lt[0]
        url_img = lt[-1]
        r = requests.get(url_img)
        f = open('images/' + name + '.jpg', 'wb')
        f.write(r.content)
        f.close()


# 数据导出CSV
def save_csv(ilt):
    name = ['姓名', '特点', '简介', '照片链接']
    f = open('teacher.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(name)
    writer.writerows(ilt)
    f.close()


if __name__ == '__main__':
    info_list = []  # 存储老师信息的列表
    url = 'http://show.ybccode.com/teachers/teachers.html'
    html = get_html_text(url)
    get_teachers_info(html, info_list)
    get_teachers_img(info_list)
    save_csv(info_list)
