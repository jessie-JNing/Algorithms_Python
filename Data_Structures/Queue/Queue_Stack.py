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


class Queue_stack(object):
    def __init__(self):
        self.stack_master = Stack()
        self.stack_assist = Stack()

    def stack_enqueue(self, item):
        self.stack_master.push(item)

    def stack_dequeque(self):
        if self.stack_isEmpty():
            return None
        while self.stack_master.size()>1:
            self.stack_assist.push(self.stack_master.pop())
        stack_value = self.stack_master.pop()

        while self.stack_assist.size()>0:
            self.stack_master.push(self.stack_assist.pop())
        return stack_value

    def stack_isEmpty(self):
        return self.stack_master.size()==0

    def __str__(self):
        display_list = []
        while self.stack_master.size() >0:
            self.stack_assist.push(self.stack_master.pop())
        while self.stack_assist.size()>0:
            value = self.stack_assist.pop()
            display_list.append(str(value))
            self.stack_master.push(value)
        return "[" + ','.join(display_list) + "]"


if __name__ == "__main__":
    queue_stack = Queue_stack()
    for i in range(5):
        queue_stack.stack_enqueue(i)
    print queue_stack

    queue_stack.stack_dequeque()
    queue_stack.stack_dequeque()
    print queue_stack