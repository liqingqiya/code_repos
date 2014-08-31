#!/usr/bin/env python
# -*- coding:utf-8 -*-

def compute_one_byte(one_byte):
    """
    计算一个字节
    """
    for i, j in enumerate(one_byte[::-1]):
        yield pow(eval(j)*2, i)

def parse_ip_str(ip_str_address):
    """
    解析ip地址
    """
    ret = ""
    for i in xrange(4):
        temp = ip_str[i*8:(i+1)*8]
        ret += str(sum(compute_one_byte(temp))) + "."
    return ret

if __name__ == "__main__":
    ip_str = "00001001111001001010100100100101"
    ret = parse_ip_str(ip_str)
    print ret
