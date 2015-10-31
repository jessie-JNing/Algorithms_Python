#!/usr/bin/env python
# encoding: utf-8

"""
A child is running up a staircase with n steps, and can hop
either 1 step, 2 steps or 3 steps at a time. Implement a mehtod
to count how many possible ways the child can run up the starts.

@author: Jessie

@email: jessie.JNing@gmail.com

"""

# naive recursion
def run_stairs(n):
    if n < 0: return 0

    elif n ==0: return 1

    else:
        return run_stairs(n-1) + run_stairs(n-2) + run_stairs(n-3)


def run_stairs_dp(n):
    cache = {}
    return _run_stairs_dp(n, cache)

def _run_stairs_dp(n, cache):
    if n < 0: return 0

    elif n==0: return 1

    else:
        cache[n] = run_stairs(n-1) + run_stairs(n-2) + run_stairs(n-3)
        return cache[n]

if __name__=="__main__":

    print "run_stairs(3): ", run_stairs(3), "-- run_stairs_dp(3): ", run_stairs_dp(3)
    print "run_stairs(4): ", run_stairs(4), "-- run_stairs_dp(4): ", run_stairs_dp(4)
    print "run_stairs(18): ", run_stairs(18), "-- run_stairs_dp(18): ", run_stairs_dp(18)