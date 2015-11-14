#!/usr/bin/env python
# encoding: utf-8

"""
Create an algorithm to check whether two trees T1 and T2 are identical.


@author: Jessie
@email: jessie.JNing@gmail.com

"""
from Tree import BinaryTree

def check_identical(T1, T2):
    if T1 is None and T2 is None:
        return True
    if T1 is None and T2 is not None or T1 is not None and T2 is None:
        return False
    else:
        if T1.getRootVal() != T2.getRootVal():
            return False
        q1 = check_identical(T1.getLeftChild(), T2.getLeftChild())
        q2 = check_identical(T1.getRightChild(), T2.getRightChild())
        return q1 and q2


if __name__=="__main__":
    r1 = BinaryTree(0)
    r1.insertLeft(1)
    r1.insertRight(3)
    r1.insertRight(5)

    r2 = BinaryTree(0)
    r2.insertLeft(1)
    r2.insertRight(3)
    r2.insertRight(5)

    print check_identical(r1, r2)
