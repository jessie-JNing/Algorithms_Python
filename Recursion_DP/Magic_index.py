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

def find_magic_naive(nums):
    for i in range(len(nums)):
        if i == nums[i]:
            return i
    return None

# find magic index in an array with duplicate elements
def find_magic_duplicate(nums):
    return _find_magic_dupliate(nums, 0, len(nums)-1)

def _find_magic_dupliate(nums, left, right):
    if left>right or left<0 or right>len(nums):
        return None

    mid = (left + right)/2
    if nums[mid] == mid:
        return mid

    # search left
    left_min = min(mid-1, nums[mid])
    left = _find_magic_dupliate(nums, left, left_min)
    if left >=0:
        return left

    right_min = min(mid+1, nums[mid])
    right = _find_magic_dupliate(nums, right_min, right)
    return right



if __name__=="__main__":
    print "find_magic_index",  find_magic_duplicate([2,2,2,5,6,7,8,9])