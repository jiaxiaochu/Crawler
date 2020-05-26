# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
from email.mime.text import MIMEText
import smtplib

msg = MIMEText('hello, Python auto send email', 'plain', 'utf-8')
# 输入Email地址和口令:
from_addr = input('请输入发件人的邮箱号码From: ')
password = input('请输入发件人的邮箱密码Password: ')
# 输入SMTP服务器地址:
smtp_server = input('请输入邮箱服务器地址SMTP server: ')
# 输入收件人地址:
to_addr = input('请输入收件人邮箱地址To: ')

import smtplib

server = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP协议加密端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
