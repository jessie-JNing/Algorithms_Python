#!/usr/bin/env python
# encoding: utf-8

"""
Given a directed graph, design an algorithm to find out whether there is a route
between two nodes.

@author: Jessie
@email: jessie.JNing@gmail.com

"""

def find_route(graph, start, end):
    visited = []
    return end in search_graph(graph, start, end, visited)

def search_graph(graph, start, end, visited):
    if start in visited:
        return visited
    elif start == end:
        visited.append(end)
        return visited
    else:
        visited.append(start)
        for node in graph[start][-1: -len(graph[start])-1: -1]:
            if node not in visited:
                search_graph(graph, node, end, visited)
        return visited



if __name__=="__main__":

    graph = {0: [1,5],\
             1: [2,3],\
             2: [4],\
             3: [4,5],\
             4: [],\
             5: []}

    print "find_route", find_route(graph, 1, 5)

