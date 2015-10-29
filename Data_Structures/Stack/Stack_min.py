#!/usr/bin/env python
# encoding: utf-8

"""

@author: Jessie

@email: jessie.JNing@gmail.com
"""


# Design a stack with function min which return the minimum element
# Push, pop and min should all operate in o(1) time


class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

class Stack_min(object):
    def __init__(self):
        self.items = []
        self.minimum = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, value):
        self.items.append(value)
        if self.minimum:
            if value <= self.minimum[-1]:
                self.minimum.append(value)
            else:
                self.minimum.append(self.minimum[-1])
        else:
            self.minimum.append(value)

    def pop(self):
        if self.items:
            if self.items[-1] == self.minimum:
                self.minimum.pop()
            return self.items.pop()
        else:
            return False


    def mini(self):
        if self.isEmpty():
            return False
        else:
            return self.minimum[-1]

    def size(self):
        return len(self.items)


    def __str__(self):
        return "[" + ','.join([str(x) for x in self.items]) + "]"