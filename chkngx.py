#!/usr/bin/python
# -*- coding:utf-8 -*-
import commands
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEText import MIMEText
import sys
import socket

class CheckNgx:
    def __init__(self):
        self.response=commands.getoutput('/opt/openresty/nginx/sbin/nginx -t')
        self.email_address=['abc@abc.com.cn','abc1@abc.com.cn','abc17@abc.com.cn','abc12@abc.com.cn']       
        skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        skt.connect(('8.8.8.8',80))
        socketIpPort = skt.getsockname()
        self.ip = socketIpPort[0]

    def ngx_normal(self):
        if 'test failed' in self.response:
            subject="%s nginx配置文件检查异常" %self.ip
            for to_list in self.email_address:
                Email(tolist=to_list,subject=subject,content=self.response).send_mail()
        else:
            msg="nginx 配置检查正常"
            return msg

class Email:
    def __init__(self,**kwargs):
        self.mail_host = 'mail.abc.com.cn'
        self.mail_user = 'alert@abc.com.cn'
        self.mail_pass = 'nihaoa'
        self.tolist=kwargs.get('tolist')
        self.subject=kwargs.get('subject')
        self.content=kwargs.get('content')

    def send_mail(self):
        me = self.mail_user
        msg = MIMEMultipart('alternative')
        msg.attach(MIMEText(self.content, 'html', 'utf-8'))
        msg['Subject'] = self.subject
        msg['From'] = me
        msg['to'] = self.tolist
        try:
            s = smtplib.SMTP()
            s.connect(self.mail_host)
            s.login(self.mail_user,self.mail_pass)
            s.sendmail(me,self.tolist,msg.as_string())
            s.close()
            return True
        except Exception,e:
            return str(e)

if __name__ == '__main__':
    print "version 1.0.0"
    print CheckNgx().ngx_normal()
