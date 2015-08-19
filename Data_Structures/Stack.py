#!/usr/bin/env python
# encoding: utf-8

"""

Stack() creates a new stack that is empty.
        It needs no parameters and returns an empty stack.

push(item) adds a new item to the top of the stack.
           It needs the item and returns nothing.

pop() removes the top item from the stack.
      It needs no parameters and returns the item. The stack is modified.

peek() returns the top item from the stack but does not remove it.
       It needs no parameters. The stack is not modified.

isEmpty() tests to see whether the stack is empty.
          It needs no parameters and returns a boolean value.

size() returns the number of items on the stack.
       It needs no parameters and returns an integer.

@author: Jessie
@email: jessie.JNing@gmail.com

"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)