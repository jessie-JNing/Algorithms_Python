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

# def search_rotated_binary(nums, item):
#