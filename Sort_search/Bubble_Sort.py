#!/usr/bin/env python
# encoding: utf-8

"""

Start at the beginning of the array and swap the first two element
if the first is greater than the second.

Then go to the next pair and so on, continuously making sweeps of the
array until it is sorted.

Runtime: o(n2) average and worst case. Memory: o(1)

@author: Jessie
@email: jessie.JNing@gmail.com

"""

# without any optimization
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    return nums


# opt_1:
# if there's no swap in the last inner loop, then it is sorted.
def bubble_sort_swapmark(nums):
    for i in range(len(nums)):
        swap_mark = False
        for j in range(1, len(nums)):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                swap_mark = True

        if not swap_mark:
            break
    return nums


# opt_2:
# record the last the position of swap, so elements after that are sorted.
def bubble_sort_lastpos(nums):
    last_pos = len(nums)
    for i in range(len(nums)):
        swap_mark = False
        for j in range(1, last_pos):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                last_pos = j
        if not swap_mark:
            break
    return nums

if __name__ == "__main__":
    unsorted = [54,26,93,17,77,31,44,55,20]
    print "bubble_sort:" , bubble_sort(unsorted)
    print "bubble_sort_swapmark:" , bubble_sort_swapmark(unsorted)
    print "bubble_sort_lastpos:" , bubble_sort_lastpos(unsorted)