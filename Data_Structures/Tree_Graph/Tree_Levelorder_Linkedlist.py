#!/usr/bin/env python
# encoding: utf-8

"""
Given a binary tree, design an algorithm which create a linked list of all the
nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked
lists)

@author: Jessie
@email: jessie.JNing@gmail.com

"""

from Tree import BinaryTree
from Data_Structures.Linked_List.Linked_List import Linked_list


# traverse binary tree in order level
def levelorder(tree):
    if tree != None:
        current_level = [tree]
        while current_level:
            next_level = []
            for node in current_level:
                if node.getRightChild():
                    next_level.append(node.getLeftChild())
                if node.getRightChild():
                    next_level.append(node.getRightChild())
            print [x.getRootVal() for x in current_level],
            current_level = next_level
