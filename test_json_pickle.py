#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json
import pickle
import ujson
import time

dictionary = dict(a=1,b=2,c=3,d=4)
print dictionary
numbers = 1000000

i = 1
lasttime = time.time()
while i < numbers:
  after_dumps = pickle.dumps(dictionary)
  after_loads = pickle.loads(after_dumps)
  i += 1
now = time.time()
print "pickle:", now-lasttime

i = 1
lasttime = time.time()
while i < numbers:
  after_dumps = json.dumps(dictionary)
  after_loads = json.loads(after_dumps)
  i += 1
now = time.time()
print "json:", now-lasttime

i = 1
lasttime = time.time()
while i < numbers:
  after_dumps = ujson.dumps(dictionary)
  after_loads = ujson.loads(after_dumps)
  i += 1
now = time.time()
print "ujson:",now-lasttime
