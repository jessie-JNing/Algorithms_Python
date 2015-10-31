#!/usr/bin/env python
# encoding: utf-8

"""
Write a method to compute all permutations of a string.
There is no duplicate elements.

if 'a', then 'a'
if 'ab', then 'ab', 'ba'
if 'abc', then 'cab', 'acb', 'abc', 'cba', 'bca', 'bac'
if 'abcd', then, '*c*a*b*', for each permutations in 'abc'

@author: Jessie

@email: jessie.JNing@gmail.com
"""

def find_permutation(string):
    if len(string) < 1:
        return []
    elif len(string) < 2:
        return [string]
    else:
        permutations = [string[0]]
        permutations = recursion_permutation(string[1:], permutations)
    return permutations

def recursion_permutation(s, p):
    if len(s)>0:
        new_p = []
        for ele in p:
            for i in range(len(ele)):
                new_p.append(ele[0:i] + s[0] + ele[i:])
            new_p.append(ele + s[0])
        return recursion_permutation(s[1:], new_p)
    else:
        return p

if __name__=="__main__":
    print "find_permutation('abc'): ", find_permutation('abcd')
