#!/usr/bin/env python
# encoding: utf-8

"""

Data structure maps the key and correspoding value, implemented by array (linkedlist) and hash function.

Hash function: remainder, fold method, mid-square method.

Collision: two or more items come to the same slot.

Collition solutions: open addressing (linear probing, quardratic probing),
                     chaining each slot to hold a reference to a collection (or chain) of items



@author: Jessie

@email: jessie.JNing@gmail.com
"""

class hash_table(object):

    def __init__(self):
        self.table_size = 11
        self.slot = [None] * self.table_size
        self.slot_value = [None] * self.table_size

    def hash_function(self, key):
        return key%self.table_size

    def rehash(self, key):
        return (key+1)%self.table_size

    def put_item(self, key, value):
        index = self.hash_function(key)
        while self.slot[index] is not None and self.slot[index]!=key:
            index = self.rehash(index)
        self.slot[index] = key
        self.slot_value[index] = value

    def get_item(self, key):
        index = self.hash_function(key)
        stop = False
        start = index
        while self.slot[index] is not None and not stop:
            if self.slot[index] == key:
                stop = True
            else:
                index = self.rehash(index)
                if index == start:
                    stop = True
        return index


    def delete_item(self, key):
        index = self.get_item(key)
        if self.slot[index] is not None:
            self.slot[index] = None
            self.slot_value[index] = None

    def get_len(self):
        count = 0
        for ele in self.slot:
            if ele is not None:
                count += 1
        return count

    def is_in(self, key):
        index = self.get_item(key)
        if self.slot[index] is not None:
            return True
        else:
            return False

    def keys(self):
        return [x for x in self.slot if x is not None]

    def items(self):
        return [(self.slot[i], self.slot_value[i]) for i in range(self.table_size) if self.slot[i]]

    def __getitem__(self,key):
        return self.slot_value[self.get_item(key)]

    def __setitem__(self,key,data):
        self.put_item(key,data)


if __name__=="__main__":
    H=hash_table()
    H[54]="cat"
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"
    print H.keys()
    print H.items()

    A = [[0, 1, 2, 3], range(4,8), range(8,12), range(12,16)]
    print A
    m, n = 0, 0
    for i in range(3, -1, -1):
        n = 0
        for j in range(4):
            print m,n, '->', i,j
            A[m][n], A[i][j] = A[i][j], A[m][n]
            n += 1
        m += 1
    print A
