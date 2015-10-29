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


def digit_sum(head_1, head_2):
    head_sum = Node(0)
    current = head_sum
    carry = 0
    while head_1 and head_2:
        each_sum = head_1.data + head_2.data + carry
        if each_sum > 9:
            current.next = Node(each_sum%10)
            carry = 1
        else:
            current.next = Node(each_sum)
            carry = 0

        head_1 = head_1.next
        head_2 = head_2.next

        current = current.next
    while head_1:
        each_sum = head_1.data + carry
        if each_sum > 9:
            current.next = Node(each_sum%10)
            carry = 1
        else:
            current.next = Node(each_sum)
            carry = 0
        head_1 = head_1.next

    while head_2:
        each_sum = head_2.data + carry
        if each_sum > 9:
            current.next = Node(each_sum%10)
            carry = 1
        else:
            current.next = Node(each_sum)
            carry = 0
        head_2 = head_2.next

    if carry == 1:
        current.next = Node(1)

    return head_sum.next
