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


def add_tail(head, item):
    '''
    add element to the tail
    :param head: head node of the linkedlist
    :param item: new node value
    :return: None
    '''

    if head is None:
        head = Node(item)
    else:
        current = head
        while current.next:
            current = current.next
        current.next = Node(item)

def add_head(head, item):
    '''
    add element to the head
    :param head: head node of the linkedlist
    :param item: new node value
    :return: None
    '''
    new_node = Node(item)
    new_node.next = head

def search(head, item):
    '''
    search for the item in the list
    :param head: head node of the linkedlist
    :param item: new node value
    :return: True or False
    '''
    current = head
    while current:
        if current.data == item:
            return True
        current = current.next
    return False

def isEmpty(head):
    '''
    test to see whether the list is empty
    :param head:
    :return:
    '''
    return head is None

def size(head):
    '''
    get the number of items in he list
    :param head:
    :return: int
    '''
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

def index(head, item):
    '''
    find the position of the item in the list
    :param head:
    :param item:
    :return: index of the item, if not found, return -1
    '''
    index = 0
    current = head
    while current:
        if current.data == item:
            return index
        index += 1
        current = current.next
    return -1

def pop(head):
    '''
    remove and return the last item in the list
    :param head:
    :return:
    '''
    if head is Node:
        return False
    elif head.next is Node:
        tail_value = head.data
        head.data = None
    else:
        current = head
        while current.next.next:
            current = current.next
        tail_value = current.next.data
        current.next = Node
    return tail_value

def pop_at(head, index):
    '''
    remove the item at the index, and return the value
    :param head:
    :param index:
    :return:
    '''
    if head is None:
        return False
    else:
        if index == 0:
            value = head.data
            head = head.next
            return value
        else:
            cur_index = 1
            previous, current = head, head.next
            while current:
                if cur_index == index:
                    previous.next = current.next
                    return current.data
                previous = current
                current = current.next
            return None


def slide(head, start, stop):
    '''
    find the items from start to stop
    :param head:
    :param start: start index
    :param stop: stop index
    :return:
    '''
    if head is None or start > stop:
        return False
    else:
        index = 0
        current = head
        slide_head = None

        while current:
            if index == start:
                slide_head = current
                slide_cur = current
            elif index == stop:
                slide_cur.next = current
                return slide_head

            if slide_cur:
                slide_cur.next = current

            current = current.next

        return slide_head

def partition(head, item):
    '''

    :param head:
    :param item:
    :return:
    '''

    guard = Node(0)
    guard.next = head
    current = head


def display(head):
    element = []
    current = head

    while current:
        element.append(str(current.data))
        current = current.next

    return "[" + ','.join(element) + "]"


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

def reverse(head):
    previous = None
    current = head
    while current:
        temp = current.next
        current.next = previous

        previous = current
        current = temp

    return previous


if __name__=="__main__":
    a1 = Node(7)
    a2 = Node(1)
    a3 = Node(6)
    a4 = Node(5)
    a5 = Node(9)
    a6 = Node(2)


    a1.next = a2
    a2.next = a3

    a4.next = a5
    a5.next = a6

    header = reverse(a1)
    print display(header)
