#!/usr/bin/env python
# encoding: utf-8

"""
For the node(i) in the heap:
parent node = i/2
left child = 2*i, right child = 2*i+1
For a max-heap: i >= 2*i and i >= 2*i+1


Runtime: o(nlgn) average, o(n2) worst case. Memory: o(lgn)

@author: Jessie
@email: jessie.JNing@gmail.com

"""

def heap_sort(num):
    start = (len(num)/2) -1
    end = len(num)

    for i in range(start, -1 ,-1):
        num = max_heapify(num, end, i)

    for i in range(end-1,0, -1):
        num[i], num[0] = num[0], num[i]
        num = max_heapify(num, i, 0)

    return num

def max_heapify(num,end, i):
    l=2 * i + 1
    r=2 * (i + 1)
    max=i
    if l < end and num[i] < num[l]:
        max = l
    if r < end and num[max] < num[r]:
        max = r
    if max != i:
        num[i], num[max] = num[max], num[i]
        max_heapify(num, end, max)
    return num

if __name__ == "__main__":
    unsorted = [54,26,93,17,77,31,44,55,20]
    print "heap_sort:" , heap_sort(unsorted)

