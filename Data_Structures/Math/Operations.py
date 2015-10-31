#!/usr/bin/env python
# encoding: utf-8

"""
Implement the multiply, subtract and divide operations for integer.
Use only the add operator.

Subtraction:
The operation a-b is the same as a+(-1)*b, however, multiply is not allow,
so we implement a negate function.

@author: Jessie

@email: jessie.JNing@gmail.com
"""

def subtraction(m, n):
    n = negate(n)
    return m + n

def negate(n):
    minus = -1 if n>0 else 1
    neg = 0
    while n != 0:
        neg += minus
        n += minus
    return neg

def multiply_positive(m, n):
    # n must be positive number
    if n==0:
        return 0
    if n&1 == 1:
        return m + multiply_positive(m, n-1)
    if n&1 == 0:
        return (multiply_positive(m, n>>1))<<1

def multiply_naive(m, n):
    if m < n:
        return multiply_naive(n, m)

    total = 0
    x = n if n>0 else negate(n)
    for i in range(x):
        total += m

    if n > 0: return total
    else: return negate(total)


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
    rest = -1
    if m>0 and n<0 or m<0 and n>0:
        signal = True
    else:
        signal = False

    m = m if m>0 else negate(m)
    n = n if n<0 else negate(n)

    while m>=0:
        m += n
        rest += 1

    if signal:
        return negate(rest)
    else:
        return rest

if __name__=="__main__":

    print "subtraction(m, n):", subtraction(54, 0)

    print "multiply:",  multiply_positive(-11, 8)
    print "multiply_naive: ", multiply_naive(-11, 8)
    print "---------------------"

    print "divide", divide(10,3)
    print "divide_naive", divide_naive(10, -2)


