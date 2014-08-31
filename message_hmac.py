#!/usr/bin/env python
#-*- coding:utf-8 -*-

import hashlib
import hmac
import pickle
import pprint

from StringIO import StringIO

def make_digest(message):
  """
  return a digest for the message
  """
  hash = hmac.new("secret-shared-key-goes-here", message, hashlib.sha1)
  return hash.hexdigest()

class SimpleObject(object):
  """
  a very simple class to demonstrate checking digests before unpickling
  """
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

#创建一个缓冲对象
out_s = StringIO()

###############################################################
#创建一个简单实验对象
o = SimpleObject("digest matches")
#将对象序列化
pickled_data = pickle.dumps(o)
#将对象序列化之后的字符串,计算签名,摘要
digest = make_digest(pickled_data)
#header
header = "%s %s"%(digest, len(pickled_data))
print "WARNING:", header

#写入到缓冲中
out_s.write(header + "\n")
out_s.write(pickled_data)

###############################################################
#创建一个简单实验对象
o = SimpleObject("digest does not matches")
#将对象序列化
pickled_data = pickle.dumps(o)
#将对象序列化之后的字符串,计算签名,摘要
digest = make_digest("not the pickled data at all")
#header
header = "%s %s"%(digest, len(pickled_data))
print "\nWARNING:", header

#写入到缓冲中
out_s.write(header + "\n")
out_s.write(pickled_data)

#刷新缓冲区
out_s.flush

#创建一个输入流
in_s = StringIO(out_s.getvalue())

#从缓冲区读数据
while True:
  first_line = in_s.readline()
  if not first_line:
    break
  incoming_digest, incoming_length = first_line.split(" ")
  incoming_length = int(incoming_length)
  print "\nREAD:", incoming_digest, incoming_length 

  incoming_pickled_data = in_s.read(incoming_length)

  actual_digest = make_digest(incoming_pickled_data)
  print "ACTUAL:", actual_digest

  if incoming_digest != actual_digest:
    print "WARNING: Data corruption"
  else:
    obj = pickle.loads(incoming_pickled_data)
    print "OK:", obj 


print 
print 
print "map <F12> :!/usr/bin/env python %"
print "that is ok"
