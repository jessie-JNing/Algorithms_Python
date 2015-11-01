#!/usr/bin/env python
# encoding: utf-8

"""

@author: Jessie
@email: jessie.JNing@gmail.com

"""
from Data_Structures.Stack import Stack
from Tree import BinaryTree

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


if __name__=="__main__":
    r = BinaryTree('a')
    print "root:", (r.getRootVal())

    r.insertLeft('b')
    print "left child:", (r.getLeftChild().getRootVal())

    r.insertRight('c')
    print "right child:", (r.getRightChild().getRootVal())

    r.getRightChild().setRootVal('hello')
    print "Reset root:", (r.getRightChild().getRootVal())

    pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    pt.postorder()  #defined and explained in the next section