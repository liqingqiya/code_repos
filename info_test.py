#!/usr/bin python
#-*- coding:utf-8 -*-

import requests

ret = requests.get(url="http://2.aliyun.ramytech.com:9002/info/1")

print type(ret)
print ret.content