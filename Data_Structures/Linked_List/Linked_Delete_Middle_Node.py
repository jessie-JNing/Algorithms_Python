#!/usr/bin/env python
# encoding: utf-8

"""
Implement an algorithm to delete a node in the middle of a single linked list,
given only access to that node.

Since we don't have access to the head.
So copy the data from the next node over to the current, and delete the next one.

@author: Jessie
@email: jessie.JNing@gmail.com

"""



class Node:
    def __init__(self,initdata):

        self.data = initdata
        self.next = None


def delete_middle_node(middle_node):
    if middle_node is None:
        return None
    elif middle_node.next is None:
        middle_node.next = Node('dummpy')

    current = middle_node
    current.data = current.next.data
    current.next = current.next.next



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

    # header = remove_duplicate(a1)
    # print "remove_duplicate: ", display(header)

    delete_middle_node(a6)
    print "remove_duplicate_inplace: ", display(a1)