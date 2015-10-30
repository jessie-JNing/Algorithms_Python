#!/usr/bin/env python
# encoding: utf-8

"""
- Dynamic programming is similar to recursion problem.
- A good way to approach such a problem is often to implement it as a normal
  recursive solution and then add the sub-problem result to cache.

- Three laws for recursion: (1) Find out the base case
                            (2) Change towards the base case
                            (3) Able to call itself.

- Bottom-up recursion and top-down recursion
- Recursive algorithms are very space inefficient.
- If the algorithm has o(n) recursive call, then it uses o(n) memory.

- Before diving into the recursive code, ask yourself how hard it would
  be to implement it iteratively.
- Discuss the trade-offs with your interviewer.


@author: Jessie

@email: jessie.JNing@gmail.com

"""

import datetime

def Fibonacci_recursion(n):
    if n < 2:
        return n
    else:
        return Fibonacci_recursion(n-1) + Fibonacci_recursion(n-2)

cache = {}
def Fibonacci_dp(n):
    if n <2:
        cache[n] = n
        return cache[n]
    else:
        if n not in cache:
            cache[n] = Fibonacci_dp(n-1) + Fibonacci_dp(n-2)
        return cache[n]

def Fibonacci_iterate(n):
    if n<2:
        return n
    else:
        cache = dict([(x,x) for x in range(2)])
        i = 2
        while i<=n:
            cache[i] = cache[i-1] + cache[i-2]
            i += 1

        return cache[n]


if __name__ == "__main__":
    print datetime.datetime.now()
    print 'Fibonacci_recursion', Fibonacci_recursion(20)
    print datetime.datetime.now()
    print "Fibonacci_dp", Fibonacci_dp(20)
    print datetime.datetime.now()
    print "Fibonacci_iterate", Fibonacci_iterate(20)
    print datetime.datetime.now()