#!/usr/bin/env python
# encoding: utf-8

"""
Swap odd and even bits in a integer with as few instructions as possible.
(e.g. bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped ...)

Hexadecimal  0xAA  --> 10101010     --> keep even bits
             0x55  --> 01010101     --> keep odd bits

0xAAAAAAAA for 32 bits machine

@author: Jessie
@email: jessie.JNing@gmail.com

"""

def swap_odd_even(A):
    print bin(A)
    keep_even = (A&(0xAA))>>1
    keep_odd = (A&(0x55))<<1

    print bin(keep_even|keep_odd)


if __name__=="__main__":
    swap_odd_even(11)