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


def slide(head, start, stop):
    if head is None or start > stop:
        return False
    else:
        index = 0
        current = head
        slide_head = None

        while current:
            if index == start:
                slide_head = current
            if index == stop-1:
                current.next = None
                return slide_head

            current = current.next
            index += 1
        return slide_head

def display(head):
    element = []
    current = head
    while current:
        element.append(str(current.data))
        current = current.next
    return "[" + ','.join(element) + "]"


if __name__=="__main__":
    a1 = Node(0)
    a2 = Node(1)
    a3 = Node(2)
    a4 = Node(3)
    a5 = Node(4)
    a6 = Node(5)


    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6

    header = slide(a1, 3, 9)
    print display(header)

