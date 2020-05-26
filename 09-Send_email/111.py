# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

index = 0


def douabn_spider():
    start_url = "https://movie.douban.com/chart"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    response = requests.get(url=start_url, headers=headers)
    # print(response)
    if response.status_code == 200:
        datas = BeautifulSoup(response.text, 'html.parser')
        list_movies = datas.find_all('div', class_="pl2")
        for movie in list_movies:
            name = movie.find('a').text.replace(" ", "").replace("\n", "")
            info = movie.find('p', class_="pl").text
            rating = movie.find('span', class_="rating_nums").text
            # print(name, rating, info)
        return name, rating, info
    else:
        print("请求失败")


def send_email(name, rating, info, sender, pwd, recevier):
    # 邮件服务器
    mailhost = 'smtp.163.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost, 25)  # 端口
    qqmail.login(sender, pwd)
    # 发送的内容
    content = '亲爱的，今天的天气是：' + name + rating + info
    message = MIMEText(content, 'plain', 'utf-8')
    # 主题
    subject = '今日天气预报'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        qqmail.sendmail(sender, recevier, message.as_string())
        return True
    except:
        return False
    qqmail.quit()


def job():
    global index
    print("当前index的值是{}".format(index))
    print('开始发送任务')
    # data = fun()
    # wether, temperature = weather_spider()
    name, rating, info = douabn_spider()
    sender = "hellojiazhixiang@163.com"  # input("请输入发件人的邮箱账号（757585105@qq.com）:")
    pwd = "jiazhixiang10712"  # input("请输入发件人的邮箱账号客户端授权码：ylackgdiytbibdbc（orrlzmvxhbbbbfdb）:")
    recevier = input("请输入收件人的邮箱账号:")

    IsSuccess = send_email(name, rating, info, sender, pwd, recevier)  # 这里需要设置发件人的账号密码以及收件人的账号
    while IsSuccess is False:
        print("邮件发送失败，正在尝试重新发送")
        IsSuccess = send_email(name, rating, info, sender, pwd, recevier)
    print('任务完成')
    index += 1


# 设置定时
schedule.every(0.1).seconds.do(job)  # 每隔{}秒钟，执行一次job函数的任务
while index != 2:
    schedule.run_pending()
    time.sleep(1)
