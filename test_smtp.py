#!/usr/bin python
#-*- coding:utf-8 -*-

import smtplib

server = smtplib.SMTP()
server.connect("smtp.qq.com")
server.login("noreply@talkyep.com","qwer123")

print "login success"
