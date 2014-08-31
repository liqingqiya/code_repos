#!/usr/bin/env python
#-*- coding:utf-8 -*-

import redis

redis_conn = None
try:
  redis_conn = redis.StrictRedis(host="127.0.0.1", port=6379, db=0)
  print "connected success"
except Exception, e:
  print "could not connect to redis"


#print "1,", redis_conn.set("session_id", "redis_value")
print "2,", redis_conn.expire("session_id", 30)

print "success"
