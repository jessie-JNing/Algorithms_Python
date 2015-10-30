#!/usr/bin/env python
# encoding: utf-8

"""
A magic index makes A[i]=i.
Given a sorted array of distinct integers, try to find a magic index,
if one exists, in array A.

@author: Jessie

@email: jessie.JNing@gmail.com
"""

def find_magic_index(nums):
    if len(nums)<1:
        return None
    else:
        mid = len(nums)/2
        if nums[mid] == mid:
            return mid
        elif nums[mid] > mid:
            return find_magic_index(nums[0:mid])
        elif nums[mid] < mid:
            return find_magic_index(nums[mid+1:])

if __name__=="__main__":
    print "find_magic_index",  find_magic_index([1,1.5,2,5,6,7,8,9])