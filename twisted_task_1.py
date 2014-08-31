# !/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

from twisted.internet import task
from twisted.internet import reactor

def runEverySecond(i=[]):
  i.append(1)
  print i

l = task.LoopingCall(runEverySecond)
l.start(0) # call every second

# l.stop() will stop the looping calls
reactor.run()