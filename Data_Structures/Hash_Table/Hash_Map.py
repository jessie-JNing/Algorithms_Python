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


class Node:
    def __init__(self,initdata):

        self.data = initdata
        self.next = None


class hash_table(object):

    def __init__(self):
        self.table_size = 11
        self.slot = [None] * self.table_size
        self.slot_value = [None] * self.table_size

    def hash_function(self, key):
        return key%self.table_size

    #def rehash(self, key):

    def put_item(self, key, value):
        hash_index = self.hash_function(key)
        if self.slot[hash_index] is None:
            self.slot[hash_index] = Node(hash_index)
            self.slot[hash_index].next = Node(key)
            self.slot_value[hash_index] = Node(hash_index)
            self.slot_value[hash_index].next = Node(value)
        else:
            current = self.slot[hash_index].next
            current_value = self.slot_value[hash_index].next
            while current.next:
                if current.data == key:
                    current_value.data = value
                    return None
                else:
                    current = current.next
                    current_value = current_value.next

            current.next = Node(key)
            current_value.next = Node(value)


    def get_item(self, key):
        hash_index = self.hash_function(key)
        if self.slot[hash_index] is None:
            return None
        else:
            current = self.slot[hash_index].next
            current_value = self.slot_value[hash_index].next
            while current:
                if current.data == key:
                    return current_value.data
                else:
                    current = current.next
                    current_value = current_value.next
            return None


    def delete_item(self, key):
        hash_index = self.hash_function(key)
        if self.slot[hash_index] is None:
            return None
        else:
            previous, current = self.slot[hash_index], self.slot[hash_index].next
            previous_value, current_value = self.slot_value[hash_index], self.slot_value[hash_index].next
            while current:
                if current.data == key:
                    previous.next = current.next
                    previous_value.next = current_value.next
                else:
                    previous, previous_value = current, current_value
                    current, current_value = current.next, current_value.next
            if self.slot[hash_index].next is None:
                self.slot[hash_index] = None
                self.slot_value[hash_index] = None


    def get_len(self):
        total = 0
        for ele in self.slot:
            if ele:
                current = ele.next
                ele_count = 0
                while current:
                    ele_count += 1
                    current = current.next
                total += ele_count
        return total

    def is_in(self, key):
        hash_index = self.hash_function(key)
        if self.slot[hash_index] is None:
            return False
        else:
            current = self.slot[hash_index].next
            current_value = self.slot_value[hash_index].next
            while current.next:
                if current.data == key:
                    return True
                else:
                    current = current.next
                    current_value = current_value.next
            return False

    def keys(self):
        key_list = []
        for ele in self.slot:
            if ele:
                current = ele.next
                while current:
                    key_list.append(current.data)
                    current = current.next
        return key_list

    def items(self):
        item_list = []
        for i in range(len(self.slot)):
            if self.slot[i]:
                current = self.slot[i].next
                current_value = self.slot_value[i].next
                while current:
                    item_list.append((current.data, current_value.data))
                    current = current.next
                    current_value = current_value.next
        return item_list

    def __getitem__(self,key):
        return self.get_item(key)

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
    print H[44]
    print H[20]

