#!/usr/bin/env python
# encoding: utf-8

"""
Given a sorted array of integers that has been rotated unknown number of times.
Try to find out the index of that element.

Input: [15,16,19,20,25,1,3,4,5,7,10,14] --> 5
        0  1  2  3  4  5 6 7 8 9 10 11
Output: 8

@author: Jessie
@email: jessie.JNing@gmail.com

"""

def search_rotated(nums, item):
    for i in range(len(nums)):
        if nums[i] == item:
            return i
    return -1

def search_rotated_binary(nums, item):
    if len(nums)<1:
        return -1
    if len(nums)<2:
        return 0

    start, end = 0, len(nums)-1
    while start<end:
        mid = (start + end)/2
        if nums[mid] == item:
            return mid

        if nums[start] < nums[mid]:
            if nums[start] < item and nums[mid] > item:
                end = mid-1
            else:
                start = mid+1
        else:
            if nums[mid] < item and nums[end] > item:
                start = mid + 1
            else:
                end = mid-1
    return -1

if __name__=="__main__":
    rotated_array = [15,16,19,20,25,1,3,4,5,7,10,14]
    print "search_rotated(19)", search_rotated(rotated_array, 1.7)
    print "search_rotated_binary(19)", search_rotated_binary(rotated_array, 1.7)
