#!/usr/bin/env python
# encoding: utf-8

"""

A binary search will start by examining the middle item.
If that item is the one we are searching for, we are done.

If the item we are searching for is greater than the middle item, we know that the entire lower half of the list.
If it is in the list, must be in the upper half.

@author: Jessie
@email: jessie.JNing@gmail.com

"""

def binary_search(alist, item):
    '''
    Implement it with while loop.
    '''
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        middle = (first + last)/2
        if alist[middle] == item:
            found = True
        elif alist[middle] > item:
            last = middle - 1
        elif alist[middle] < item:
            first = middle + 1
    return found


def binary_search_recursive(alist, item):
    '''
    Implement it with recursion.
    '''
    if len(alist) < 1:
        return False
    else:
        middle = len(alist)/2
        if alist[middle] == item:
            return True
        elif alist[middle] > item:
            return binary_search_recursive(alist[:middle], item)
        elif alist[middle] < item:
            return binary_search_recursive(alist[middle+1:], item)


if __name__ == "__main__":
    unsorted = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print "heap_sort:" , binary_search_recursive(unsorted, 44)
