#!/usr/bin python
#-*- coding:utf-8 -*-

import torndb

db = torndb.Connection("localhost", " ", "root", "19911010")

ret = db.query("select * from auth_user;")

print ret 
print type(ret)
