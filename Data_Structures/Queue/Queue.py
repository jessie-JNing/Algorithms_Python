#!/usr/bin/env python
# encoding: utf-8

"""

Queue() creates a new queue that is empty.
        It needs no parameters and returns an empty queue.

enqueue(item) adds a new item to the rear of the queue.
              It needs the item and returns nothing.

dequeue() removes the front item from the queue.
          It needs no parameters and returns the item. The queue is modified.

isEmpty() tests to see whether the queue is empty.
          It needs no parameters and returns a boolean value.

size() returns the number of items in the queue.
       It needs no parameters and returns an integer.

@author: Jessie
@email: jessie.JNing@gmail.com

"""

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return '[' + ','.join([str(x) for x in self.items]) + ']'


