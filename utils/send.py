"""
何恺悦 hekaiyue 2023-07-06
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import logging

class Send:
    def __init__(self, parent):
        self.parent = parent
        self.smtp_basic = None
        self.smtp = None
        self.tasks = None
    
    def login(self):
        self.smtp_basic = self.parent.config.config["basic"]
        smtp_server = self.smtp_basic["smtp_server"]
        smtp_port = self.smtp_basic["smtp_port"]
        smtp_user = self.smtp_basic["smtp_user"]
        smtp_password = self.smtp_basic["smtp_password"]

        try:
            # 连接到 SMTP 服务器，并登录到发件人邮箱
            self.smtp = smtplib.SMTP_SSL(smtp_server, int(smtp_port))
            # self.smtp.set_debuglevel(1)#打印出和SMTP服务器交互的所有信息。
            self.smtp.login(smtp_user, smtp_password)
            logging.info(f"已连接到SMTP服务器，登录信息为：{str(self.smtp_basic)}")
        except Exception as e:
            logging.info(f"SMTP服务器连接失败，登录信息为：{str(self.smtp_basic)}")
            return False
        except smtplib.SMTPAuthenticationError:
            logging.info(f"SMTP服务器登陆失败，登录信息为：{str(self.smtp_basic)}")
            return False
        
        return True

    def send_multipal(self):

        def send_single_email(task):
            # 获取到任务信息
            send_from = task["from"]
            send_to = task["to"]
            send_cc = task["cc"]
            send_subject = task["subject"]
            send_body = task["body"]
            send_file = task["file"]

            logging.info(f"邮件任务已启动，任务内容为：{str(task)}，该邮件将由{str(self.smtp_basic)}进行发送")

            # 构造邮件 发件人、收件人、抄送人、正文、邮件内容
            msg = MIMEMultipart()
            msg['From'] = send_from
            msg['To'] = ", ".join(send_to)
            if len(send_cc) != 0:
                msg["Cc"] = ", ".join(send_cc)
            if send_subject != "":
                msg['Subject'] = send_subject
            if send_body != "":
                msg.attach(MIMEText(send_body, 'html'))
            if send_file != "":     # 打开文件并作为附件上传
                file_name, file_ext = os.path.splitext(os.path.basename(send_file))
                _send_file = open(f"{send_file}", 'rb').read()
                attachment = MIMEApplication(_send_file, _subtype=file_ext.strip("."))
                attachment.add_header('Content-Disposition', 'attachment', filename=f"{file_name}{file_ext}")
                msg.attach(attachment)

            # 发送邮件
            try:
                self.smtp.sendmail(send_from, send_to + send_cc, msg.as_string())
                logging.info(f"邮件发送成功！发送信息：{str(self.smtp_basic)}发送内容：{str(task)}")
            except Exception as e:
                logging.info(f"邮件发送失败！发送信息：{str(self.smtp_basic)}发送内容：{str(task)}")
                return False
            
            return True

        self.tasks = self.parent.config.config["tasks"]
        for task in self.tasks:
            send_single_email(task)

    def send_task(self):
        self.login()
        self.send_multipal()
        self.smtp.quit()
