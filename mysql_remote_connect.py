#!/usr/bin python
#-*- coding:utf-8 -*-

import peewee

myDB = peewee.MySQLDatabase("test", host="....", port=3306, user="...", passwd="...")

class BaseModel(peewee.Model):
    """A base model"""
    class Meta:
        database = myDB

myDB.connect()
print "success"