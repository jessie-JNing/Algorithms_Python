#!/usr/bin/env python
# encoding: utf-8

"""
Implement a function to check if a binary tree is a binary search tree.

@author: Jessie
@email: jessie.JNing@gmail.com

"""

from Tree import BinaryTree

def check_BST(tree):
    if tree:

        if tree.getLeftChild():
            if tree.getLeftChild().getRootVal() <= tree.getRootVal():
                check_BST(tree.getLeftChild())
            else:
                return False

        if tree.getRightChild():
            if tree.getRightChild().getRootVal() >= tree.getRootVal():
                check_BST(tree.getRightChild())
            else:
                return False

        return True

if __name__=="__main__":
    r = BinaryTree(0)
    print "root:", (r.getRootVal())

    r.insertLeft(1)
    print "left child:", (r.getLeftChild().getRootVal())

    r.insertRight(3)
    print "right child:", (r.getRightChild().getRootVal())

    r.insertRight(5)
    print "right child:", (r.getRightChild().getRootVal())

    print check_BST(r)
