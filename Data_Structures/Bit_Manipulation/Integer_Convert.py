#!/usr/bin/env python
# encoding: utf-8

"""

@author: Jessie

@email: jessie.JNing@gmail.com
"""

def bit_count_one(n):
    count = 0
    while n>0:
        count += 1
        n = n & (n-1)
    return count

def bit_count_zero(n):
    print ~0
    print n^(~0)
    return bit_count_one(n^(~0))


if __name__=="__main__":
    #print bit_count_one(14)
    print bit_count_zero(14)
