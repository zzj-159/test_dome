#!/usr/bin/python
# encoding=utf-8
# Filename: send_email.py
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
import smtplib
import time
from config.config import ReadConfig
import os


class SendEmail:
    # 构造函数：初始化基本信息
    def __init__(self, host, user, passwd):
        lInfo = user.split("@")
        self._user = user
        self._account = lInfo[0]
        self.config = ReadConfig()
        self._me = self._account + "<" + self._user + ">"

        server = smtplib.SMTP_SSL(host)
        server.connect(host)
        server.login(self._account, passwd)
        self._server = server

        # 发送文件或html邮件

    def sendTxtMail(self, to_list, subtype='html'):
        # 如果发送的是html邮件，则_subtype设置为html
        msg = MIMEMultipart()
        # a = os.getcwd()
        # print(a)
        path = os.getcwd() + "./report/reporthtml/report.html"
        path = "D:/test-loanorder_19/report/report.html"
        f = open(path, 'rb')
        mail_body = f.read().decode().encode('utf-8')
        f.close()
        mail_body2 = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        # 配置邮件主题（标题）
        msg['Subject'] = "发送邮件测试"
        msg['Subject'] = Header("接口自动化测试报告" + "_" + tm, 'utf-8')
        msg['From'] = self.config.get_conf('mail','VALUE_SENDER')
        receivers = self.config.get_conf('mail','VALUE_RECEIVER')
        toclause = receivers.split(',')
        msg['To'] = ",".join(toclause)
        msg.attach(mail_body)
        msg.attach(mail_body2)
        try:
            self._server.sendmail(self._me, to_list, msg.as_string())
            return True
        except Exception as e:
            print(str(e))
            return False

    # 发送带附件的文件或html邮件
    def sendAttachMail(self, to_list, subtype='html'):
        # 创建一个带附件的实例
        msg = MIMEMultipart()
        # pdfFile = '../report//report.html'
        # pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
        # pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
        # msg.attach(pdfApart)
        msgAlternative = MIMEMultipart('alternative')
        msg.attach(msgAlternative)
        # 邮件正文内容
        mail_body = """
                 <p>你好，Python 邮件发送测试...</p>
                 <p>这是使用python登录邮箱发送HTML格式和图片的测试邮件：</p>
                 <p>图片演示：</p>
                 <p>![](cid:send_image)</p>
                """
        # msg.attach(MIMEText(mail_body, 'html', 'utf-8'))
        msgText = (MIMEText(mail_body, 'html', 'utf-8'))
        msgAlternative.attach(msgText)

        # 指定图片为当前目录
        fp = open('./report.pdf', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # 定义图片 ID，在 HTML 文本中引用
        msgImage.add_header('Content-ID', '<send_image>')
        msg.attach(msgImage)

        try:
            self._server.sendmail(self._me, to_list, msg.as_string())
            return True
        except Exception as e:
            print(str(e))
            return False

    # 发送带附件的文件或html邮件
    def sendImageMail(self, to_list, sub, content, subtype='html'):
        # 创建一个带附件的实例
        msg = MIMEMultipart()
        # 增加邮件内容
        msg.attach(MIMEText(content, _subtype=subtype, _charset='utf-8'))

        msg['Subject'] = sub
        msg['From'] = self._me
        msg['To'] = ";".join(to_list)

        try:
            self._server.sendmail(self._me, to_list, msg.as_string())
            return True
        except Exception as e:
            print(str(e))
            return False

    # 析构函数：释放资源
    def __enter__(self):
        self._server.quit()
        self._server.close()


mailto_list = ['zzj18851176320@163.com']
mail = SendEmail('smtp.sino-bridge.com', 'zhangzhj@sino-bridge.com', 'Qwer123')
if mail.sendTxtMail(mailto_list, "测试邮件"):
    print("发送成功")
else:
    print("发送失败")

# if mail.sendImageMail(mailto_list, "测试邮件-带一个图片的附件", "hello world！<br><br><h1>你好，发送文本文件测试<h1>"):
#     print("发送成功")
#
# else:
#     print("发送失败")




