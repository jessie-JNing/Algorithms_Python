#!/usr/bin/env python
# encoding: utf-8

"""

@author: Jessie
@email: jessie.JNing@gmail.com

"""
from Data_Structures.Stack.Stack import Stack
from Data_Structures.Queue.Queue import Queue

from Graph import Vertex
from Graph import Graph

def breadth_first_search(graph, root):
    if graph is None:
        return None

    visited = []
    queue = Queue()
    queue.enqueue(root)

    while not queue.isEmpty():
        current = queue.dequeue()
        if current not in visited:
            visited.append(current)
            for node in graph[current]:
                if node not in visited:
                    queue.enqueue(node)
    return visited


def depth_first_search(graph, root):

    if graph is None:
        return None

    visited = []
    saved_nodes = Stack()
    saved_nodes.push(root)

    while not saved_nodes.isEmpty():
        current = saved_nodes.pop()
        if current not in visited:
            visited.append(current)
            for node in graph[current]:
                if node not in visited:
                    saved_nodes.push(node)
    return visited

def depth_first_search_recursion(graph, root):

    if graph is None:
        return []

    visited = []
    return _depth_first_search_recursion(graph, root, visited)

def _depth_first_search_recursion(graph, root, visited):
    if root in visited:
        return visited

    visited.append(root)
    for node in graph[root][-1: -len(graph[root])-1: -1]:
        if node not in visited:
            _depth_first_search_recursion(graph, node, visited)
    return visited


if __name__=="__main__":

    graph = {0: [1,5],\
             1: [0,2,3],\
             2: [1,4],\
             3: [1,4,5],\
             4: [2,3,4],\
             5: [0,3,3]}

    print "depth_first_search", depth_first_search(graph, 0)
    print "depth_first_search_recursion", depth_first_search_recursion(graph, 0)

    print "breadth_first_search", breadth_first_search(graph, 0)
