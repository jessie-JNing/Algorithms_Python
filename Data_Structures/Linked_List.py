#!/usr/bin/env python
# encoding: utf-8

"""

OrderedList() creates a new ordered list that is empty.
              It needs no parameters and returns an empty list.

add(item) adds a new item to the list making sure that the order is preserved.
          It needs the item and returns nothing. Assume the item is not already in the list.

remove(item) removes the item from the list.
             It needs the item and modifies the list. Assume the item is present in the list.

search(item) searches for the item in the list.
             It needs the item and returns a boolean value.

isEmpty() tests to see whether the list is empty.
          It needs no parameters and returns a boolean value.

size() returns the number of items in the list.
       It needs no parameters and returns an integer.

index(item) returns the position of item in the list.
            It needs the item and returns the index. Assume the item is in the list.

pop() removes and returns the last item in the list.
      It needs nothing and returns an item. Assume the list has at least one item.

pop(pos) removes and returns the item at position pos.
         It needs the position and returns the item. Assume the item is in the list.

@author: Jessie
@email: jessie.JNing@gmail.com

"""

class Node:
    def __init__(self,initdata):

        self.data = initdata
        self.next = None

    def getData(self):

        return self.data

    def getNext(self):

        return self.next

    def setData(self,newdata):

        self.data = newdata

    def setNext(self,newnext):

        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        if self.size()==0:
            temp.setNext(self.head)
            self.head = temp
            self.tail = temp

        else:
            temp.setNext(self.head)
            self.head = temp

    def slide(self, start, stop):
        link_slide = UnorderedList()
        current = self.head
        promote = False
        while current!=None:
            if current.getData() == start:
                promote = True
            elif current.getData() == stop:
                break
            if promote == True:
                link_slide.add(current.getData())
            current = current.getNext()
        return link_slide

    def __str__(self):
        element = []
        current = self.head
        while current!= None:
            element.append(str(current.getData()))
            current = current.getNext()
        return  "[" + ','.join(element) + "]"


    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        app = Node(item)
        self.tail.setNext(app)
        self.tail = app

    def index(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        return previous.getData()

    def list_pop(self):
        current = self.head
        previous = None
        while current!= None:
            previous = current
            current = current.getNext()
        if previous == None:
            self.head = current.getNext()
            return current
        else:
            previous.setNext(current.getNext())
            return current

