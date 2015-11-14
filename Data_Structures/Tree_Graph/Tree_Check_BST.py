#!/usr/bin/env python
# encoding: utf-8

"""
Implement a function to check if a binary tree is a binary search tree.

Assume a BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

@author: Jessie
@email: jessie.JNing@gmail.com

"""

from Tree import BinaryTree

#-------------------------------------------------------------
# give upper and lower bound
def isValidBST(root):
    return isValidBSTRec(root, float("-infinity"), float("infinity"))

def isValidBSTRec(root, min, max):
    if root == None:
        return True
    if root.getRootVal()<=min or root.getRootVal()>=max:
        return False
    left = isValidBSTRec(root.getLeftChild(), min, root.getRootVal())
    right = isValidBSTRec(root.getRightChild(), root.getRootVal(), max)
    return left and right

#-------------------------------------------------------------
def valid_BST(root):
    path = _valid_BST(root, [])
    for i in range(1, len(path)):
        if path[i-1]>path[i]:
            return False
    return True


def _valid_BST(root, path):
    if root is None:
        return None
    _valid_BST(root.getLeftChild(), path)
    path.append(root.getRootVal())
    _valid_BST(root.getRightChild(), path)
    return path




if __name__=="__main__":
    r = BinaryTree(20)
    print "root:", (r.getRootVal())

    r.insertLeft(10)
    print "left child:", (r.getLeftChild().getRootVal())

    r.insertRight(30)
    print "right child:", (r.getRightChild().getRootVal())

    r.getLeftChild().insertRight(25)
    print r.getLeftChild().getRightChild().getRootVal()

    print valid_BST(r)
