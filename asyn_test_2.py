# !/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

import time

from twisted.internet import defer, reactor
from twisted.web.client import getPage

times = 100000000

def syn_compute(times=times):
  """
  同步计算
  :return:
  """
  begin_time = time.time()
  b = 0
  for i in range(times):
    b += i
  b = 0
  for i in range(times):
    b += i
  over_time = time.time()
  print "function:%s, use time:%s"%(syn_compute.__name__, over_time-begin_time)


def asyn_compute(times=times):
  """
  异步计算
  :param times:
  :return:
  """
  begin_time = time.time()
  d = defer.Deferred()
  d.callback(times)
  d.addCallback(function_1)
  d.addCallback(function_2)
  over_time = time.time()
  print "function:%s, use time:%s"%(asyn_compute.__name__, over_time-begin_time)
  reactor.run()

def function_1(times):
  b = 0
  for i in range(times):
    b += i
  print "function:%s, b:%s, time:%s"%(function_1.__name__, b, time.time())
  return times

def function_2(times):
  b = 0
  for i in range(times):
    b += i
  print "function:%s, b:%s, time:%s"%(function_2.__name__, b, time.time())

if __name__ == "__main__":
  syn_compute()
  asyn_compute()
