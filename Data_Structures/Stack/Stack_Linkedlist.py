#!/usr/bin/env python
# encoding: utf-8

"""

@author: Jessie

@email: jessie.JNing@gmail.com
"""

# implement stack with linkedlist
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

class Stack_Linkedlist(object):
    def __init__(self):
        self.head = Node(0)

    def isEmpty(self):
        return self.head.next is None

    def push(self, item):
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(item)

    def pop(self):
        if self.isEmpty():
            return False
        else:
            current = self.head
            while current.next.next:
                current = current.next
            value = current.next.data
            current.next = current.next.next
        return value

    def peak(self):
        if self.isEmpty():
            return Node
        else:
            current = self.head
            while current.next:
                current = current.next
            return current.data

    def __str__(self):
        display_list = []
        current = self.head.next
        while current:
            display_list.append(str(current.data))
            current = current.next
        return "[" + ','.join(display_list) + "]"