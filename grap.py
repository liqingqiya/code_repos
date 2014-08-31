#!/usr/bin/env python
#-*- coding:utf-8 -*-

from functools import wraps

def memo(func):
  cache = {}
  @wraps(func)
  def wrap(*args):
    if args not in cache:
      cache[args] = func(*args)
    return cache[args]
  return wrap

def rec_dag_sp(w,s,t):
  @memo
  def d(u):
    if u==t:
      return 0
    return min(w[u][v]+d(v) for v in w[u])

if __name__ == "__main__":
  w = {0:{1:2,5:9}, 1:{2:1,3:2,5:6}, 2:{3:7}, 3:{4:2,5:3}, 4:{5:4}, 5:{}}
s, t = 0, 5
print rec_dag_sp(w,s,t)
