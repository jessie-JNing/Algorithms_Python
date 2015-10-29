#!/usr/bin/env python
# encoding: utf-8

"""

@author: Jessie

@email: jessie.JNing@gmail.com
"""

class Node(object):
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

class Queue_Linkedlist(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def enqueque(self, item):
        if self.isEmpty():
            self.head = Node(item)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(item)

    def dequeue(self):
        if self.isEmpty():
            return False
        else:
            value = self.head.data
            self.head = self.head.next
            return value

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        display_list = []
        current = self.head
        while current:
            display_list.append(str(current.data))
            current = current.next
        return "[" + ','.join(display_list) + "]"