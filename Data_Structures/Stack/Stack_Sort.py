#!/usr/bin/env python
# encoding: utf-8

"""

@author: Jessie

@email: jessie.JNing@gmail.com
"""

# need modify
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


def stack_sort_space(unsorted_stack):

    temp_stack = Stack()
    while not unsorted_stack.isEmpty():
        temp_value = unsorted_stack.pop()

        counter = 0
        while not temp_stack.isEmpty():
            if temp_stack.peak() < temp_value:
                unsorted_stack.push(temp_stack.pop())
                counter += 1
            else:
                break
        temp_stack.push(temp_value)
        for i in range(counter):
            temp_stack.push(unsorted_stack.pop())

    while not temp_stack.isEmpty():
        unsorted_stack.push(temp_stack.pop())

    return unsorted_stack

def stack_merge_sort(unsorted_stack):
    if unsorted_stack.size()<2:
        return unsorted_stack
    else:
        # divide the stack into two
        left_stack = Stack()
        right_stack = Stack()
        while not unsorted_stack.isEmpty():
            left_stack.push(unsorted_stack.pop())
            if not unsorted_stack.isEmpty():
                right_stack.push(unsorted_stack.pop())

        left_stack = stack_merge_sort(left_stack)
        right_stack = stack_merge_sort(right_stack)
        return stack_merge(left_stack, right_stack)

def stack_merge(left, right):
    combine_stack = Stack()
    while not left.isEmpty() and not right.isEmpty():
        if left.peak()>right.peak():
            combine_stack.push(left.pop())
        else:
            combine_stack.push(right.pop())

    while not left.isEmpty():
        combine_stack.push(left.pop())
    while not right.isEmpty():
        combine_stack.push(right.pop())
    #-----------------------------------------
    # remember to change the order back using another stack
    back_stack = Stack()
    while not combine_stack.isEmpty():
        back_stack.push(combine_stack.pop())
    #-----------------------------------------
    return back_stack


if __name__== "__main__":

    random_stack = Stack()
    for i in range(0,8,2):
        random_stack.push(i)
    for i in range(1,8,2):
        random_stack.push(i)

    print random_stack

    print stack_merge_sort(random_stack)
