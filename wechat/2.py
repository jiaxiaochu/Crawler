import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

account = input('请输入你的邮箱：')
password = input('请输入你的密码：')
receiver = input('请输入收件人的邮箱：')


def get_weather():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}  # 封装headers
    url = 'http://www.weather.com.cn/weather/101020100.shtml'  # 把URL链接赋值到变量url上
    res = requests.get(url, headers=headers)  # 发送requests请求，并把响应的内容赋值到变量res中
    res.encoding = 'utf-8'  # 转码
    bsdata = BeautifulSoup(res.text, 'html.parser')
    data_temperature = bsdata.find(class_='wea')
    data_weather = bsdata.find(class_='tem')


def send_email(tem, wea, sender, pwd, recevier):
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost, 25)
    qqmail.login(sender, pwd)

    content = '亲爱的，今天的天气是：' + tem + wea
    message = MIMEText(content, 'piain', 'utf-8')
    try:
        qqmail.sendmail(sender, recevier, message.as_string())
        return True
    except:
        return False
    qqmail.quit()


def job():
    print('开始第一次发送任务')
    tem, wea = get_weather()
    sender = input("请输入发件邮箱：")
    pwd = input("请输入发件邮箱密码(授权码)：")
    recevier = input("请输入收件邮箱：")
    IsSuccess = send_email(tem, wea, sender, pwd, recevier)
    while IsSuccess is False:
        print("邮件发送失败，正在尝试重新发送")
        IsSuccess = send_email(tem, wea, sender, pwd, recevier)
    print('任务完成')


schedule.every().day.at("10：30").do(job)

while True:
    schedule.run_pending()

    time.sleep(1)
