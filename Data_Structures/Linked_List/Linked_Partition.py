#!/usr/bin/env python
# encoding: utf-8

"""
Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x.

@author: Jessie
@email: jessie.JNing@gmail.com

"""

class Node(object):
    def __init__(self,initdata):

        self.data = initdata
        self.next = None

class Linked_list(object):
    def __init__(self):
        self.link_head = None

    def add_tail(self, item):
        current = self.link_head
        while current.next:
            current = current.next
        current.next = item

    def add_head(self, item):
        item.next = self.link_head
        self.link_head = item

def partition_linkedlist_biadd(head, pivot):
    par_linked = Linked_list()
    par_linked.link_head = Node(pivot)

    current = head
    while current:
        #temp = current
        if current.data > pivot:
            par_linked.add_tail(Node(current.data))
            #par_linked.add_tail(temp)
        else:
            #par_linked.add_head(temp)
            par_linked.add_head(Node(current.data))
        current = current.next
    return par_linked.link_head

def partition_array(nums, pivot):

    left, right = 0, len(nums)-1
    while left< right:

        while nums[left] <= pivot:
            left += 1
        while nums[right] >= pivot:
            right -= 1

        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums[:left] + [pivot] + nums[left:]


def partition_linkedlist(head, pivot):
    less = Node("less")
    more = Node("more")

    less_cur, more_cur, current = less, more, head
    while current:
        if current.data < pivot:
            less_cur.next = Node(current.data)
            less_cur = less_cur.next
        else:
            more_cur.next = Node(current.data)
            more_cur = more_cur.next
        current = current.next

    less_cur.next = more.next

    return less.next

def partition_linkedlist_inplace(head, pivot):
    less = Node("less")
    more = Node("more")

    less_cur, more_cur, current = less, more, head
    while current:
        if current.data < pivot:
            less_cur.next = current
            less_cur = less_cur.next
        else:
            more_cur.next = current
            more_cur = more_cur.next
        current = current.next

    more_cur.next = None
    less_cur.next = more.next

    return less.next


def display(head):
    element = []
    current = head
    while current:
        element.append(str(current.data))
        current = current.next
    return "[" + ','.join(element) + "]"

if __name__ == "__main__":
    unsorted = [54,26,93,17,77,31,44,55,20]
    print "partition_array:" , partition_array(unsorted, 24)

    a1 = Node(54)
    a2 = Node(26)
    a3 = Node(93)
    a4 = Node(17)
    a5 = Node(77)
    a6 = Node(31)


    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6

    header = partition_linkedlist_biadd(a1, 43)
    print "partition_linkedlist", display(header)