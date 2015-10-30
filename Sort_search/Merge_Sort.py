#!/usr/bin/env python
# encoding: utf-8

"""
Merge sort divides the array in half, sort each of those halves and then merges them together.
Each of those halves has the same sorting algorithm applied to it.

Two steps:
- Divide: divide the array into halves recursively
- Merge: two finger method sort two halves

Runtime: o(nlgn) average and worst case. Memory: depends

@author: Jessie
@email: jessie.JNing@gmail.com

"""

def merge_sort(nums):
    if len(nums) <2 : return nums

    mid = len(nums)/2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)



def merge(lnums, rnums):
    merge_nums = []
    i,j = 0,0

    while i<len(lnums) and j<len(rnums):
        if lnums[i] < rnums[j]:
            merge_nums.append(lnums[i])
            i += 1
        elif lnums[i] > rnums[j]:
            merge_nums.append(rnums[j])
            j += 1

    if i < len(lnums): merge_nums.extend(lnums[i:])
    if j < len(rnums): merge_nums.extend(rnums[j:])

    return merge_nums

if __name__ == "__main__":
    unsorted = [54,26,93,17,77,31,44,55,20]
    print "merge_sort:" , merge_sort(unsorted)