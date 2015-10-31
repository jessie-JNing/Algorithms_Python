#!/usr/bin/env python
# encoding: utf-8

"""
Write a function to determine the number of bit required to convert integer A to B
For example:  12  1 1 0 0
              10  1 0 1 0
               ^  0 1 1 0

@author: Jessie
@email: jessie.JNing@gmail.com

"""
def integer_convert(A, B):
    # calculate the number of digits in these two numbers are different.
    C = A ^ B
    counter = 0
    while C > 0:
        counter += (C&1)
        C = C>>1
    return counter

if __name__=="__main__":
    print "integer_convert(12, 10)", integer_convert(12, 10)