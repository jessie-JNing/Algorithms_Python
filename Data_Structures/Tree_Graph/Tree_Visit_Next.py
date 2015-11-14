#!/usr/bin/env python
# encoding: utf-8

"""
Write a algorithm to find the "next" node of a given node in a binary search tree.
You may assume that each node has a link to its parent.


@author: Jessie
@email: jessie.JNing@gmail.com

"""

from Tree import BinaryTree

#-----------------------------------------------
# inorder traverse and find the next one
def find_next(tree, item):
    path = inorder(tree, [])
    for i in range(len(path)-1):
        if path[i] == item:
            return path[i+1]
    return None

def inorder(tree, path):
    if tree:
        inorder(tree.getLeftChild(), path)
        path.append(tree.getRootVal())
        inorder(tree.getRightChild(), path)
        return path
    else:
        return path

#-----------------------------------------------
# find the next in different cases
def find_next_cases(tree):
    if tree is None:
        return None
    else:
        if tree.getRightChild():
            return left_more(tree.getRightChild())
        else:
            current = tree
            par = current.getParent()
            while par and par.getLeftChild() is not current:
                par = par.getParent()
            return par


def left_more(tree):
    if tree is None:
        return None
    else:
        while tree.getLeftChild():
            tree = tree.getLeftChild()
        return tree


if __name__=="__main__":
    r = BinaryTree(0)
    print "root:", (r.getRootVal())

    r.insertLeft(1)
    print "left child:", (r.getLeftChild().getRootVal())

    r.insertRight(3)
    print "right child:", (r.getRightChild().getRootVal())

    r.insertRight(5)
    print "right child:", (r.getRightChild().getRootVal())


    print find_next(r, 5)