#!/usr/bin/env python
# encoding: utf-8

"""
Pick a random element and partition the array, so that all numbers that are
less than partition come before, and larger than partition come after.

The partitioning is performed through swaps.


Runtime: o(nlgn) average, o(n2) worst case. Memory: o(lgn)

@author: Jessie
@email: jessie.JNing@gmail.com

"""
def quick_sort(nums):
    if len(nums) < 2: return nums
    else:
        _quicksort(nums, 0, len(nums)-1)
        return nums

def _quicksort(array, start, stop):
    if stop - start > 0:
        pivot, left, right = array[start], start, stop
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _quicksort(array, start, right)
        _quicksort(array, left, stop)

if __name__ == "__main__":
    unsorted = [54,26,93,17,77,31,44,55,20]
    print "quick_sort:" , quick_sort(unsorted)