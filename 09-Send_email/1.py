import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email():
    smtp = 'smtp.qq.com'
    sender = '757585105@qq.com'
    password = 'mreqaxgmvonjbfdb'
    # receiver = ['1072022525@qq.com', '757585105@qq.com', 'hellojiazhixiang@163.com']
    receiver = ['757585105@qq.com', 'hellojiazhixiang@163.com']  # , 'jiazhixiang@fenbi.com']

    # 创建MIMEMultipart对象，采用related定义内嵌资源
    # message = MIMEMultipart('related')
    message = MIMEMultipart()

    message['Subject'] = '测试定时发送邮件-这是用程序发送的附件邮件哦'
    message['From'] = '猿编程<757585105@qq.com>'
    message['To'] = '猿宝们'

    content = '''<html>
    <h1>hello world ...</h1>
    <p><img src="cid:image"></p>
    </html>
    '''
    # content = '''<html><body><h1>测试图片发送</h1><img src="cid:image" alt="image"></body></html>'''
    message_text = MIMEText(content, 'html', 'utf-8')
    message.attach(message_text)

    # f = open('./1.png', 'rb')
    # image_data = f.read()
    # f.close()

    with open('./1.png', 'rb') as f:
        image_data = f.read()

    image = MIMEImage(image_data)
    # image.add_header('Content-ID', 'image')
    image.add_header('Content-Disposition', 'attachment', filename=('GBK', '', '状猿.png'))
    message.attach(image)

    # f2 = open('北京景点信息.xlsx', 'rb')
    # excel_data = f2.read()
    # f2.close()

    with open('./北京景点信息.xlsx', 'rb') as f2:
        excel_data = f2.read()

    excel_file = MIMEApplication(excel_data)
    excel_file.add_header('Content-Disposition', 'attachment', filename=('GBK', '', '北京景点信息.xlsx'))
    message.attach(excel_file)

    content = message.as_string()
    server = smtplib.SMTP_SSL(smtp, 465)
    server.login(sender, password)
    print('正在发送邮件 . . .')
    server.sendmail(sender, receiver, content)
    server.quit()
    print('邮件发送成功')


def print_time():
    now = time.ctime()
    print(now)


scheduler = schedule.Scheduler()
# scheduler.every().minute.do(send_email)  # 每分钟执行一次send_email函数
scheduler.every().minute.at(':30').do(send_email)  # 每分钟执行一次send_email函数
scheduler.every(10).seconds.do(print_time)  # 每10秒执行一次print_time函数
while True:
    scheduler.run_pending()
