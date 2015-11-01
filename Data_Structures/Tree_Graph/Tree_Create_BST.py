#!/usr/bin/env python
# encoding: utf-8

"""
Given a sorted array(increasing order) with unique integer element, write an
algorithm to crease a binary search tree with nimimal height.
@author: Jessie
@email: jessie.JNing@gmail.com

"""
from Tree import BinaryTree
from Tree_Traverse import *
from Tree_Check_BST import check_BST


def crease_BST(nums):
    tree = BinaryTree("")
    start, end = 0, len(nums)-1
    _crease_BST(nums, tree, start, end)
    return tree

def _crease_BST(nums, tree, start, end):
    if start > end:
        return None
    else:
        mid = (start + end)/2
        tree.setRootVal(nums[mid])
        if start<=mid-1:
            tree.insertLeft("")
            _crease_BST(nums, tree.getLeftChild(), start, mid-1)
        if mid+1<=end:
            tree.insertRight("")
            _crease_BST(nums, tree.getRightChild(), mid+1, end)


if __name__=="__main__":
    sorted_list = range(8)
    BST = crease_BST(sorted_list)

    preorder(BST)
    print ''
    inorder(BST)
    print ''
    levelorder(BST)
