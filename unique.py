#!/usr/bin/python
#-*- coding:utf-8 -*-

def unique(s):
    '''
    消除重复
    '''
    l = list(s)
    l.sort()
    return [x for i,x in enumerate(l) if not i or x!=l[i-1]]

if __name__ == "__main__":
    print unique("abccdas")
