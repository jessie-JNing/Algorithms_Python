#!/usr/bin/env python
# encoding: utf-8

"""
Given an MXN matrix in which each row and each column is sorted in ascending order.
Write a method to find an element.

@author: Jessie
@email: jessie.JNing@gmail.com

"""

def search_matrix(M, item):
    for i in range(len(M)):
        col = binary_search(M[i], item)
        if col>-1:
            return (i, col)
    return (-1, -1)

def binary_search(nums, item):
    start, end = 0, len(nums)-1

    while start<=end:
        mid = (start+end)/2
        if nums[mid]==item:
            return mid
        elif nums[mid] > item:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def search_matrix_saving(M, item):
    row, col = 0, len(M[0])-1
    while row<len(M) and col>=0:
        if M[row][col] == item:
            return (row, col)
        if M[row][col] > item:
            col -= 1
        elif M[row][col] < item:
            row += 1
    return (-1, -1)




if __name__=="__main__":
    matrix = [[15,20,40,85],
              [20,35,80,93],
              [30,55,95,105],
              [40,80,100,120]]

    print "search_matrix(93)", search_matrix(matrix, 93)
    print "search_matsearch_matrix_savingrix(93)", search_matrix_saving(matrix, 93)