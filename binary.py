#!/usr/bin/python
#-*- coding:utf-8 -*-

a = 5523

def parseint(n):
    """
    解析出整数的数字
    """
    cache = []
    while n:
        div, mod = divmod(n, 10)
        cache.append(mod)
        n = div
    cache.reverse()
    return cache

def ten2N(n, N=2):
    cache = []
    while n:
        div, mod = divmod(n, N)
        cache.append(mod)
        n = div
    cache.reverse()
    return cache

def two2ten(n):
    """
    二进制转换为十进制
    """
    cache = []
    temp = parseint(n)
    temp_1 = range(len(temp))
    temp_1.reverse()
    for i, j in zip(temp, temp_1):
        if i!=0:
            ret = pow(2*i, j)
            cache.append(ret)
    return sum(cache)


if __name__ == "__main__":
    ret = parseint(a)
    print ret
    ret = ten2N(12, 8)
    print ret
    ret = two2ten(111)
    print ret

