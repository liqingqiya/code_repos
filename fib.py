#!/usr/bin/env python
#-*- coding:utf-8 -*-

from functools import wraps

def memo(func):
  cache = {}
  @wraps(func)
  def wrap(*args):
    print "args:", args
    print "cache:", cache
    if args not in cache:
      cache[args] = func(*args)
    return cache[args]
  return wrap

@memo
def fib(i):
  if i<2:return 1
  return fib(i-1) + fib(i-2)

if __name__ == "__main__":
    print fib(8)
