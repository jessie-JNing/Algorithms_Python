#!/usr/bin/env python
# encoding: utf-8

"""
Implement an algorithm to find the kth to last element of a singly linked list.

We define k, such that passing k = 1, return the last element.
                               k = 2, return the second to last element
                               k = 0, return the last element.

if k > len(linklist), return the first element.

@author: Jessie
@email: jessie.JNing@gmail.com

"""


class Node:
    def __init__(self,initdata):

        self.data = initdata
        self.next = None

#----------------------------------------------
# recursion
def find_kth(head, k):
    if head:
        i = find_kth(head.next, k) + 1
        if i==k:
            print 'the kth,',head.data
        return i
    else:
        return 0

#----------------------------------------------
# non-recursion
def find_kth_iteration(head, k):
    if head is None:
        return head
    else:
        fast, slow = head, head
        counter = 0
        while fast:
            if counter < k:
                fast = fast.next
                counter += 1
            else:
                fast = fast.next
                slow = slow.next

        return slow.data



def display(head):
    element = []
    current = head
    while current:
        element.append(str(current.data))
        current = current.next
    return "[" + ','.join(element) + "]"



if __name__ == "__main__":
    a1 = Node(0)
    a2 = Node(1)
    a3 = Node(2)
    a4 = Node(3)
    a5 = Node(4)
    a6 = Node(5)


    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6

    print find_kth_iteration(a1, 1)
    #print "remove_duplicate_inplace: ", display(header)