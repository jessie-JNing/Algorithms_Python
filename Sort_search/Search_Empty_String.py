#!/usr/bin/env python
# encoding: utf-8

"""

Given a sorted array of strings which is interspersed with empty string,
write a method to find the location of a give string.

@author: Jessie
@email: jessie.JNing@gmail.com

"""

def search_empty(nums, item):
    for i in range(len(nums)):
        if nums[i] == item:
            return i
    return -1

def search_empty_binary(nums, item):

    start, end = 0, len(nums)-1
    while start < end:
        mid = (start + end)/2
        if nums[mid] =='':
            mid = find_mid(nums, mid, start, end)
        if nums[mid] == item:
            return mid
        elif nums[mid] < item:
            start = mid + 1
        else:
            end = mid-1
    return -1

def find_mid(nums, mid, start, end):
    left, right = mid-1, mid+1
    while start <= left and right <= end:
        if nums[right]!="":
            return right
        if nums[left]!="":
            return left
        left -=1
        right += 1
    return -1

def search_empty_binary_recursion(nums, item):
    return _search_empty_binary_recursion(nums, item, 0, len(nums)-1)

def _search_empty_binary_recursion(nums, item, start, end):

    if start>end:
        return False

    mid = (start + end)/2
    if nums[mid] =='':
        mid = find_mid(nums, mid, start, end)
    if nums[mid] == item:
        return mid
    elif nums[mid] < item:
        return _search_empty_binary_recursion(nums, item, mid+1, end)
    else:
        return _search_empty_binary_recursion(nums, item, start, mid-1)


if __name__=="__main__":
    rotated_array = [1,'','','',2,'','',3, 4,'',5,'',6,'','','',7,9]
    print "search_rotated(6)", search_empty(rotated_array,5)
    print "search_empty_binary(6)", search_empty_binary(rotated_array, 5)
    print "search_empty_binary_recursion(6)", search_empty_binary_recursion(rotated_array, 5)
