#/usr/bin/env python
#-*- coding:utf-8 -*-

def jiebao(obj):
  try:
    for i in obj.values():
      if isinstance(i,dict):
        yield i
      else:
        for k in jiebao(i):
          yield k
  except Exception:
    yield None

def skip_password(obj):
  ret={}
  try:
    for k in obj:
      if k not in ["password", "Password", "PASSWORD"]:
        ret[k]=dict[k]
    for k in ret:
      if isinstance(ret[k], dict):
        skip_password(ret[k])
    return ret
  except TypeError:
    return obj
  
if __name__ == "__main__":
  obj = {"a":12,"b":[1,2,3],"$set":{"password":"3121214"}}
  print obj
  print "============================================"
  for i, j in enumerate(jiebao(obj)):
    print i," : ",j
  print "============================================"
  print skip_password(obj)
