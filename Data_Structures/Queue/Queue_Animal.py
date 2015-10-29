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

class Queue_Animal(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def animal_enqueue(self, item):
        if self.isEmpty():
            self.head = Node(item)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(item)

    def animal_dequeueAny(self):
        if self.isEmpty():
            return False
        else:
            value = self.head.data
            self.head = self.head.next
            return value

    def animal_dequeueEither(self, carOdog):
        if self.isEmpty():
            return False
        else:
            value = "there is no " + carOdog
            if carOdog in self.head.data:
                value = self.head.data
                self.head = self.head.next
            else:
                previous = self.head
                current = self.head.next
                adopted = False
                while current:
                    if not adopted and carOdog in current.data:
                        value = current.data
                        previous.next = current.next
                        adopted = True
                    previous = current
                    current = current.next
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

if __name__=="__main__":
    queue_animal = Queue_Animal()
    queue_animal.animal_enqueue("cat0")
    queue_animal.animal_enqueue("cat1")
    queue_animal.animal_enqueue("dog0")
    queue_animal.animal_enqueue("dog1")
    queue_animal.animal_enqueue("cat2")
    queue_animal.animal_enqueue("cat3")
    print queue_animal

    print queue_animal.animal_dequeueAny()
    print queue_animal

    print queue_animal.animal_dequeueEither("cat")
    print queue_animal

    print queue_animal.animal_dequeueEither("cat")
    print queue_animal

    print queue_animal.animal_dequeueEither("cat")
    print queue_animal

    print queue_animal.animal_dequeueEither("cat")
    print queue_animal

