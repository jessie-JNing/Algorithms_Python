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


# whether a single linked list has circle inside
def has_circle(head):
    if head and head.next:
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    else:
        return False

# find the entrance of the circle
def find_entrance(head):
    if head and head.next:
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
    else:
        return None

    slow = head
    while slow:
        slow = slow.next
        fast = fast.next
        if slow == fast:
            return slow.data

# whether two single linkedlists(no circle) intersect
def is_intersect(head1, head2):
    if head1 and head2:
        current_1 = head1
        while current_1:
            current_1 = current_1.next
        current_2 = head2
        while current_2:
            current_2 = current_2.next
        return current_1 == current_2

    return False


# whether two single linkedlists(have circle) intersect
# find the node that fast and slow pointer meet
# if the node in the other linkedlist, then they intersect
def is_intersect_circle(head1, head2):
    # find the meeting node in circle
    if head1 and head1.next:
        slow, fast = head1, head1
        while fast:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        current = head2
        while current:
            if current == slow:
                return True
            current = current.next

    return False


if __name__ == "__main__":
    a1 = Node(54)
    a2 = Node(26)
    a3 = Node(93)
    a4 = Node(17)
    a5 = Node(77)
    a6 = Node(31)


    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6
    a6.next = a2

    print find_entrance(a1)