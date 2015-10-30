#!/usr/bin/env python
# encoding: utf-8

"""
A child is running up a staircase with n steps, and can hop
either 1 step, 2 steps or 3 steps at a time. Implement a mehtod
to count how many possible ways the child can run up the starts.

@author: Jessie

@email: jessie.JNing@gmail.com

"""

def runup_stairs(n):
    if n < 1:
        return None

    if n == 1:
        return 1

    if n == 2:
        return 2

    if n == 3:
        return 3

    if n > 3:
        return (runup_stairs(n-1)+1) + (runup_stairs(n-2)+2) + (runup_stairs(n-3)+4)

if __name__=="__main__":
    print "runup_stairs(3): ", runup_stairs(3)
    print "runup_stairs(4): ", runup_stairs(4)
    print "runup_stairs(8): ", runup_stairs(8)