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

class Linked_list(object):
    def __init__(self):
        self.head = None

    def add_tail(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(item)

    def add_head(self, item):
        new_head = Node(item)
        new_head.next = self.head
        self.head = new_head

    def isEmpty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


    def index(self, item):
        index = 0
        current = self.head
        while current:
            if current.data == item:
                return index
            index += 1
            current = current.next
        return -1

    def pop(self):
        if self.isEmpty():
            return False
        elif self.head.next is None:
            tail_value = self.head.data
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            tail_value = current.next.data
            current.next = None
        return tail_value

    def pop_at(self, index):
        if self.isEmpty():
            return False
        else:
            if index == 0:
                value = self.head.data
                self.head = self.head.next
                return value
            else:
                cur_index = 1
                previous, current = self.head, self.head.next
                while current:
                    if cur_index == index:
                        previous.next = current.next
                        return current.data
                    previous = current
                    current = current.next
                    cur_index += 1
                return None

    def search(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False


    def __str__(self):
        element = []
        current = self.head
        while current:
            element.append(str(current.data))
            current = current.next
        return "[" + ','.join(element) + "]"



if __name__=="__main__":

    linked_list = Linked_list()
    for i in range(9):
        linked_list.add_tail(i)
    print linked_list

    for i in range(11,78,11):
        linked_list.add_head(i)
    print linked_list

    linked_list.pop()
    print linked_list

    linked_list.pop_at(3)
    print linked_list

    linked_list.pop_at(0)
    print linked_list
