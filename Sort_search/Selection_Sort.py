#!/usr/bin/env python
# encoding: utf-8

"""

Find the smallest element using a linear scan and move it to the front.
Then find the second smallest and move it.

Runtime: o(n2) average and worst case. Memory: o(1)

@author: Jessie
@email: jessie.JNing@gmail.com

"""

def selection_sort(nums):
    for i in range(len(nums)-1):
        minimum = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[minimum]:
                minimum = j
        nums[i], nums[minimum] = nums[minimum], nums[i]
    return nums

if __name__ == "__main__":
    unsorted = [54,26,93,17,77,31,44,55,20]
    print "selection_sort:" , selection_sort(unsorted)