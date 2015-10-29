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




class set_of_stacks(object):
    def __init__(self):
        self.stacks = [Stack()]
        self.threshold = 10

    def set_push(self, item):
        if self.stacks[-1].size() >= self.threshold:
            self.stacks.append(Stack())

        self.stacks[-1].push(item)

    def set_pop(self):
        if self.set_isEmpty():
            return None
        else:
            set_value = self.stacks[-1].pop()
            return set_value

    def set_pop_At(self, index):
        if self.set_isEmpty() or self.set_size()<index or self.stacks[index].isEmpty():
            return None

        set_value = self.stacks[index].pop()
        return set_value

    def set_isEmpty(self):
        return self.stacks[0].isEmpty()

    def set_size(self):
        total_size = 0
        for sta in self.stacks:
            total_size += sta.size()
        return total_size

    def __str__(self):
        total_stack = []
        for sta in self.stacks:
            total_stack.append(str(sta))
        return '->'.join(total_stack)


if __name__=="__main__":

    Stack_Set = set_of_stacks()

    for i in range(17):
        Stack_Set.set_push(i)

    print Stack_Set

    print Stack_Set.set_pop()

    print Stack_Set
