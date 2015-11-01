#!/usr/bin/env python
# encoding: utf-8

"""
Implement a function to check if a binary tree is balanced.

Balanced Tree: height(left) - height(right) = -1, 0, 1

@author: Jessie
@email: jessie.JNing@gmail.com

"""
from Tree import BinaryTree

def traverse_node(tree):
    if tree:
        # visit the current root node
        height_delta = check_height(tree, 0, 0)
        if abs(height_delta[0] - height_delta[1]) < 2:
            traverse_node(tree.getLeftChild())
            traverse_node(tree.getRightChild())
        else:
            return False
        return True
    else:
        return False

def check_height(tree, left_height, right_height):
    if not tree.getLeftChild() and not tree.getRightChild():
        return (0, 0)
    if tree.getLeftChild():
        left_height = check_height(tree.getLeftChild(), left_height, right_height)[0] + 1
    if tree.getRightChild():
        right_height = check_height(tree.getRightChild(), left_height,right_height)[1] + 1

    return (left_height, right_height)


if __name__=="__main__":
    r = BinaryTree('a')
    print "root:", (r.getRootVal())
    r.insertLeft('b')
    print "left child:", (r.getLeftChild().getRootVal())
    r.insertRight('c')
    print "right child:", (r.getRightChild().getRootVal())
    r.insertRight('d')
    print "right child:", (r.getRightChild().getRootVal())
    r.insertRight('e')
    print "right child:", (r.getRightChild().getRootVal())


    print "traverse_node\n", traverse_node(r)
