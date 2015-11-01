#!/usr/bin/env python
# encoding: utf-8

"""

@author: Jessie
@email: jessie.JNing@gmail.com

"""
class Vertex(object):
    def __init__(self, id):
        self.id = id
        self.connectedTo = []

    def add_neighbor(self, neighbor):
        self.connectedTo.append(neighbor)

    def get_connections(self):
        return self.connectedTo

    def __str__(self):
        return str(self.id)+' connectedTo: ' + str([x.id for x in self.connectedTo])

class Graph(object):
    def __init__(self):
        self.vert_dict = {}
        self.vertice_no = 0

    def add_vertice(self,key):
        self.vertice_no += 1
        new_vertex = Vertex(key)
        self.vert_dict[key] = new_vertex
        return new_vertex

    def add_edge(self, start, end):
        if start not in self.vert_dict:
            self.add_vertice(start)
        if end not in self.vert_dict:
            self.add_vertice(end)
        self.vert_dict[start].add_neighbor(self.vert_dict[end])
        self.vert_dict[end].add_neighbor(self.vert_dict[start])

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None



if __name__=="__main__":
    graph = Graph()
    for i in range(6):
        graph.add_vertice(i)

    for i in range(5):
        graph.add_edge(i, i+1)
    graph.add_edge(5, 0)

    for i in range(4):
        graph.add_edge(i, i+2)
    graph.add_edge(4,0)
    graph.add_edge(5,1)

    for i in range(graph.vertice_no):
        print graph.vert_dict[i]


