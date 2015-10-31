#!/usr/bin/env python
# encoding: utf-8

"""
Write a method to return all subsets of a set.

A = set(a)           --> subsets: (a)
B = set(a,b)         --> subsets: (b), + (b)*set(a)
C = set(a,b,c)       --> subsets: (c), + (c)*set(a,b)

@author: Jessie

@email: jessie.JNing@gmail.com
"""

def find_subsets(elements):
    subsets = [[]]
    if len(elements)>0:
        subsets = recursion_subset(elements, subsets)
    return subsets

def recursion_subset(ele, subsets):
    if len(ele)>0:
        new = []
        for i in range(len(subsets)):
            new.append(subsets[i] + [ele[0]])
        subsets.extend(new)
        return recursion_subset(ele[1:], subsets)
    else:
        return subsets



if __name__=="__main__":
    print "find_subsets([1,2,3]): ", find_subsets([1,2,3,4])