#!/usr/bin/env python
# encoding: utf-8

"""
Implement the multiply, subtract and divide operations for integer.
Use only the add operator

@author: Jessie

@email: jessie.JNing@gmail.com
"""

def multiply(m, n):
    if n==0:
        return 0
    if n&1 == 1:
        return m + multiply(m, n-1)
    if n&1 == 0:
        return (multiply(m, n>>1))<<1

def multiply_naive(m, n):
    total = 0
    for i in range(n):
        total += m
    return total

def divide(m, n):
    rest = 0
    while m >= n:
        divisor = n
        i = 1
        while m >= divisor:
            m -= divisor
            rest += i

            divisor <<= i
            i <<= 1
    return rest

def divide_naive(m, n):
    rest = 0
    while m>=n:
        m -=n
        rest += 1

    return rest


if __name__=="__main__":

    print "multiply:",  multiply(11, 8)
    print "multiply_naive: ", multiply_naive(11, 8)
    print "---------------------"

    print "divide", divide(10,3)
    print "divide_naive", divide_naive(10, 3)


