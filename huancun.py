#!/usr/bin/python
#-*- coding:utf-8 -*-

from functools import wraps

def bibao(fn):
    cache = {}
    @wraps(fn)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = fn(*args)
            return cache[args]
    return wrapper

if __name__ == "__main__":

    @bibao
    def f(x):
        return 2*x

    a =f(2)
    print a



