#!/usr/bin/env python
# encoding: utf-8

"""
We begin by assuming that a list with one item (position 0) is already sorted.

On each pass, one for each item 1 through n−1, the current item is checked against
those in the already sorted sublist.

We shift those items that are greater to the right.
When we reach a smaller item or the end of the sublist, the current item can be inserted.

Runtime: o(n2) average and worst case. Memory: o(1)

@author: Jessie
@email: jessie.JNing@gmail.com

"""

# sort it into increasing order
def insertion_sort(nums):
    if len(nums) < 2:
        return nums
    else:
        for i in range(1, len(nums)):
            insert_ele = nums[i]
            j = i
            while j>0:
                if nums[j-1] > insert_ele:
                    nums[j] = nums[j-1]
                    j -=1
                else:
                    break
            nums[j] = insert_ele
        return nums



if __name__ == "__main__":
    unsorted = [54,26,93,17,77,31,44,55,20]
    print "insertion_sort:" , insertion_sort(unsorted)