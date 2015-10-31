#!/usr/bin/env python
# encoding: utf-8

"""
Remove duplicates from an unsorted linked list.
- In order to remove duplicate from an unsorted list, use a hash table to track duplicates.

FOLLOW UP: solve this problem if temporary buffer is not allowed?
- If there's no extra buffer, we can iterate with two pointers:
  current: run through the linked list
  runner: check duplicate in subnodes.

@author: Jessie
@email: jessie.JNing@gmail.com

"""

class Node:
    def __init__(self,initdata):

        self.data = initdata
        self.next = None


#----------------------------------------------
# time o(n), space o(n)
def remove_duplicate(head):
    tracking = {}
    guard = Node(0)
    guard.next = head

    previous, current = guard, head
    while current:
        if current.data in tracking:
            previous.next = current.next
        else:
            tracking[current.data] = True
            previous = current

        current = current.next

    return guard.next
#----------------------------------------------


#----------------------------------------------
# time o(n^2), space o(1)
def remove_duplicate_inplace(head):

    outer_current = head
    while outer_current:

        inner_pre = outer_current
        inner_cur = outer_current.next
        while inner_cur:
            if inner_cur.data == outer_current.data:
                inner_pre.next = inner_cur.next
            else:
                inner_pre = inner_cur
            inner_cur = inner_cur.next

        outer_current = outer_current.next

    return head



def display(head):
    element = []
    current = head
    while current:
        element.append(str(current.data))
        current = current.next
    return "[" + ','.join(element) + "]"



if __name__ == "__main__":
    a1 = Node(0)
    a2 = Node(0)
    a3 = Node(2)
    a4 = Node(2)
    a5 = Node(2)
    a6 = Node(3)


    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6

    # header = remove_duplicate(a1)
    # print "remove_duplicate: ", display(header)

    header = remove_duplicate_inplace(a1)
    print "remove_duplicate_inplace: ", display(header)




