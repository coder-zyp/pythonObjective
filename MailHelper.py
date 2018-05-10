#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务

mail_user = "250074114@qq.com"  # 用户名
mail_pass = "vjfbrrsicccycaij"  # 口令
receivers = ['coder_zyp@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
message = MIMEText(text, 'plain', 'utf-8')
message['From'] = Header(mail_user, 'utf-8')
message['To'] = Header(receivers[0], 'utf-8')
message['Subject'] = Header('邮件测试标题', 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
    # smtpObj.connect()  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(mail_user, receivers, message.as_string())
    smtpObj.quit()
    print("邮件发送成功")


except smtplib.SMTPException as e:
    print("Error: 无法发送邮件", e)


# # with 的使用
# # 普通版本
# file = open("/tmp/foo.txt")
# data = file.read()
# file.close()
#
# # 加入抛异常 缺点  try内失败会导致，finally会崩溃 ，例如   NameError: name 'file' is not defined
# try:
#     file = open("/tmp/foo.txt")
#     data = file.read()
# finally:
#     file.close()
#
#
# # 如果要打开文件并保证最后关闭他，只需要这么做：
# with open("/tmp/foo.txt") as file:
#     data = file.read()