#!/usr/bin/env python
# encoding: utf-8

"""
Use a single array to implement three stacks.

@author: Jessie
@email: jessie.JNing@gmail.com

"""

# stack_1: A[:n/3], stack_2: A[n/3: 2*n/3], stack_3: A[2*n/3, n]

class Stack(object):
    def __init__(self):
        self.stack_size = 100
        self.items = [False]*self.stack_size
        self.counter = [0, self.stack_size/3, 2*self.stack_size/3]

    def isEmpty(self, k):
        left, right = (k-1)*self.stack_size/3, k*self.stack_size/3
        for i in range(left, right):
            if self.items[i]:
                return False
        return True

    def push(self, k, item):
        position = self.counter[k]
        self.items[position] = item
        self.counter[k] += 1

    def pop(self, k):
        if self.counter[k] < (k-1)*self.stack_size/3:
            return None
        else:
            position = self.counter[k]-1
            value = self.items[position]
            self.items[position] = False
            return value

    def size(self, k):
        sub_size = 0
        left, right = (k-1)*self.stack_size/3, k*self.stack_size/3
        for i in range(left, right):
            if self.items[i]:
                sub_size += 1
        return sub_size

    def __str__(self):
        return "[" + ','.join([str(x) for x in self.items]) + "]"
