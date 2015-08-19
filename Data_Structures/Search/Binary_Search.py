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
    :param alist: an ordered list
    :param item: the item needs to be searched
    :return: True if found.
    A binary search will start by examining the middle item. If that item is the one we are searching for, we are done.
    If it is not the correct item, we can use the ordered nature of the list to eliminate half of the remaining items.
    '''
    first = 0
    last = len(alist)
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
    :param alist: an ordered list
    :param item: the item needs to be searched
    :return: True if found.
    Implement it in recursive function
    A binary search will start by examining the middle item. If that item is the one we are searching for, we are done.
    If it is not the correct item, we can use the ordered nature of the list to eliminate half of the remaining items.
    '''
    middle = len(alist)/2
    if alist[middle] == item:
        return True
    elif len(alist) <2:
        return False
    else:
        if alist[middle] > item:
            return binary_search_recursive(alist[:middle], item)
        elif alist[middle] < item:
            return binary_search_recursive(alist[middle+1:], item)
