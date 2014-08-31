#!/usr/bin python
#-*- coding:utf-8 -*-

from itertools import product

def compute(er_cha_iterable):
    er_cha_iterable = map(str, er_cha_iterable)
    temp_tuple = product(er_cha_iterable,"-", er_cha_iterable)
    for item in temp_tuple:
        tmp = "".join(item)
        ret = abs(eval(tmp))
        yield ret

if __name__ == "__main__":
    er_cha_test = [1,2,12,4,5]
    ret = max(compute(er_cha_test))
    print ret
