#!/usr/bin/env python
# encoding: utf-8

"""

@author: Jessie
@email: jessie.JNing@gmail.com

"""

class Node:
    def __init__(self,initdata):

        self.data = initdata
        self.next = None

# use extra space
def check_palindrome(head):
    if head is None:
        return False

    refer_list = []
    current = head
    while current:
        refer_list.append(current.data)
        current = current.next

    current = head
    while current:
        if current.data != refer_list.pop():
            return False
    return True


def check_palindrome_twopointer(head):
    if head is None:
        return False
    if head.next is None:
        return True

    if head and head.next:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        # check for the rest of the linked list


def display(head):
    element = []
    current = head
    while current:
        element.append(str(current.data))
        current = current.next
    return "[" + ','.join(element) + "]"


if __name__ == "__main__":
    a1 = Node(0)
    a2 = Node(1)
    a3 = Node(2)
    a4 = Node(3)
    a5 = Node(4)
    a6 = Node(5)
    a7 = Node(6)

    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6
    a6.next = a7

    header = check_palindrome_twopointer(a1)
