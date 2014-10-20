#!/usr/bin/python
#-*- coding:utf-8 -*-

def unique1(s, f=None):
    if f is None:
        def f(x):return x
    already = []
    for i in s:
        if f(i) not in already:
            already.append(i)
    return already

if __name__ == "__main__":
    print unique1("abbcaaddde")

