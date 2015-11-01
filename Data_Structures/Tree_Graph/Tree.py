#!/usr/bin/env python
# encoding: utf-8

"""
Given a sorted array(increasing order) with unique integer element, write an
algorithm to crease a binary search tree with nimimal height.
@author: Jessie
@email: jessie.JNing@gmail.com

"""

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key





if __name__=="__main__":
    r = BinaryTree(0)
    print "root:", (r.getRootVal())

    r.insertLeft(1)
    print "left child:", (r.getLeftChild().getRootVal())

    r.insertRight(3)
    print "right child:", (r.getRightChild().getRootVal())

    r.insertRight(5)
    print "right child:", (r.getRightChild().getRootVal())
