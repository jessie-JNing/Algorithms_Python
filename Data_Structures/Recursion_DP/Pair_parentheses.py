#!/usr/bin/env python
# encoding: utf-8

"""
Implement an algorithm to print all valid combinations of n-pairs of parentheses.

Input: 3
Output: ((())); ((),()); (())(); ()(()); ()()()

@author: Jessie

@email: jessie.JNing@gmail.com
"""

def pair_parentheses(n):
    if n < 1:
        return []
    elif n < 2:
        return ["()"]
    else:
        parentheses = ["()"]
        parentheses = recursion_parentheses(n-1, parentheses)
        return parentheses

def recursion_parentheses(x, par):
    if x > 0:
        new_par = []
        for ele in par:
            new_par.extend(["(" + ele + ")", "()"+ ele, ele+ "()"])
        return recursion_parentheses(x-1, set(new_par))
    else:
        return par

if __name__ == "__main__":
    print "pair_parentheses(1):", pair_parentheses(1)
    print "pair_parentheses(2):", pair_parentheses(2)
    print "pair_parentheses(3):", pair_parentheses(3)
    print "pair_parentheses(4):", pair_parentheses(4)
