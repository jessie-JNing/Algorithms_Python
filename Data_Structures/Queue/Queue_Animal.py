#!/usr/bin/env python
# encoding: utf-8

"""

@author: Jessie

@email: jessie.JNing@gmail.com
"""

from Queue import Queue
# use array, two queues

class Animal(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def cat_or_dog(self):
        if "cat" in self.name:
            return "cat"
        elif "dog" in self.name:
            return "dog"
        else:
            return None

class Queue_Animal_array(object):
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()
        self.count = 0

    def animal_enqueue(self, item):
        animal = Animal(item, self.count)
        if animal.cat_or_dog() == "cat":
            self.cat.enqueue(animal)
            self.count += 1
        elif animal.cat_or_dog() == "dog":
            self.dog.enqueue(animal)
            self.count += 1
        else:
            return None
    
    def animal_dequeueAny(self):
        if self.cat.isEmpty() and self.dog.isEmpty():
            return None
        elif self.cat.isEmpty() and not self.dog.isEmpty():
            return self.dog.dequeue()
        elif not self.cat.isEmpty() and self.dog.isEmpty():
            return self.cat.dequeue()
        else:
            cat = self.cat.peak().id
            dog = self.dog.peak().id
            if cat<dog:
                return self.cat.dequeue()
            else:
                return self.dog.dequeue()
    
    def animal_dequeueCat(self):
        if self.cat.isEmpty():
            return None
        else:
            return self.cat.dequeue()
        
    def animal_dequeueDog(self):
        if self.dog.isEmpty():
            return None
        else:
            return self.dog.dequeue()




class Node(object):
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

# use linked list, implement two queue
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
    queue_animal = Queue_Animal_array()
    queue_animal.animal_enqueue("cat0")
    queue_animal.animal_enqueue("dog101")
    queue_animal.animal_enqueue("dog0")
    queue_animal.animal_enqueue("dog1")
    queue_animal.animal_enqueue("cat2")
    queue_animal.animal_enqueue("cat3")
    print queue_animal

    ani = queue_animal.animal_dequeueAny()
    print ani.id, ani.name

    ani = queue_animal.animal_dequeueAny()
    print ani.id, ani.name

    ani = queue_animal.animal_dequeueCat()
    print ani.id, ani.name

    ani = queue_animal.animal_dequeueCat()
    print ani.id, ani.name
