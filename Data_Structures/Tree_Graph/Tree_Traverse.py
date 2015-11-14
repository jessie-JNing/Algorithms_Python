#!/usr/bin/env python
# encoding: utf-8

"""

@author: Jessie
@email: jessie.JNing@gmail.com

"""

from Data_Structures.Linked_List.Linked_List import Linked_list

def preorder(tree):
    if tree:
        print(tree.getRootVal()),
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal()),

def inorder(tree):
      if tree != None:
          inorder(tree.getLeftChild())
          print(tree.getRootVal()),
          inorder(tree.getRightChild())

def levelorder(tree):
    if tree != None:
        current_level = [tree]
        while current_level:
            next_level = []
            for node in current_level:
                if node.getLeftChild():
                    next_level.append(node.getLeftChild())
                if node.getRightChild():
                    next_level.append(node.getRightChild())
            print [x.getRootVal() for x in current_level],
            current_level = next_level

def level_order_linkedlist(tree):
    if tree is not None:
        current = Linked_list()
        current.add_head(tree)
        while current:
            next = Linked_list()
            next_head = next
            node = current.head
            while node:
                if node.data.getLeftChild():
                    next.add_tail(node.data.getLeftChild())
                if node.data.getRightChild():
                    next.add_tail(node.data.getRightChild())
                node = node.next
            print node
            current = next
