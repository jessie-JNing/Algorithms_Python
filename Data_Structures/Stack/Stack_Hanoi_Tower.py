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

    def size(self):
        return len(self.items)

    def __str__(self):
        return "[" + ','.join([str(x) for x in self.items]) + "]"


def Hanoi_Tower(tower_1, tower_2, tower_3):
    if tower_1.size() == 1:
        tower_3.push(tower_1.pop())
        print tower_3
    elif tower_1.size() == 2:
        tower_2.push(tower_1.pop())
        tower_3.push(tower_1.pop())
        tower_3.push(tower_2.pop())
        print tower_3
    else:
        pass



if __name__=="__main__":
    stack_1 = Stack()
    stack_2 = Stack()
    stack_3 = Stack()
    stack_1.push(2)
    stack_1.push(1)
    stack_1.push(0)


    Hanoi_Tower(stack_1, stack_2, stack_3)