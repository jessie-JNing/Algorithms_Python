#!/usr/bin/env python
# encoding: utf-8

"""

@author: Jessie

@email: jessie.JNing@gmail.com
"""


class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

    def peak(self):
        if self.isEmpty():
            return None
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return "[" + ','.join([str(x) for x in self.items]) + "]"


def stack_sort(unsorted_stack):
    temp_stack = Stack()

    for i in range(unsorted_stack.size()):
        # find the smallest element in stack
        minimum = unsorted_stack.peak()
        while unsorted_stack.size() > i:
            temp_value = unsorted_stack.pop()
            if temp_value < minimum:
                minimum = temp_value
            temp_stack.push(temp_value)

        # push the smallest element to the bottom
        # the has_put flag to prevent duplicate element being lost
        unsorted_stack.push(minimum)
        has_put = False
        while temp_stack.size() > 0:
            temp_value = temp_stack.pop()
            if not has_put and temp_value == minimum:
                has_put = True
            else:
                unsorted_stack.push(temp_value)

    return unsorted_stack

if __name__== "__main__":

    random_stack = Stack()
    for i in range(0,8,2):
        random_stack.push(i)
    for i in range(1,8,2):
        random_stack.push(i)

    random_stack.push(6)
    print random_stack

    print stack_sort(random_stack)
