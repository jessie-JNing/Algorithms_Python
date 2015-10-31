#!/usr/bin/env python
# encoding: utf-8

"""
You are given two sorted arrays, A and B, where A has a large enough buffer at the end
to hold B.

Write a method to merge B into A in sorted order.

@author: Jessie
@email: jessie.JNing@gmail.com

"""
# create new array
def merge_two_sorted(A, B):
    merged = []
    i, j = 0,0
    while i<len(A) and j<len(B):
        if A[i]<B[j]:
            merged.append(A[i])
            i +=1
        else:
            merged.append(B[j])
            j +=1
    if i < len(A): merged.extend(A[i:])
    if j < len(B): merged.extend(B[j:])

    return merged

# insert into A
def merge_two_sorted_insert(A, B):
    i = 0
    while i < len(B):
        current = B[i]
        A.append(current)
        j = len(A)-1
        while j >0:
            if A[j-1]>B[i]:
                A[j] = A[j-1]
                j -= 1
            else:
                break
        A[j] = current
        i += 1
    return A

# insert into A
def merge_two_sorted_another(A, B):
    i, j = len(A)-1, len(B)-1
    A.extend([0]* len(B))
    k = len(A)-1

    while i >=0 and j >=0:
        if A[i] > B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1

    while j >= 0:
        A[k] = B[j]
        j -= 1
        k -= 1

    return A


if __name__ == "__main__":
    A = [1,3,5,7,9]
    B = [2,4,6,8]
    print "merge_two_sorted:" , merge_two_sorted(A, B)
    #print "merge_two_sorted_insert:" , merge_two_sorted_insert(A, B)
    print "merge_two_sorted_another", merge_two_sorted_another(A, B)
