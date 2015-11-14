#!/usr/bin/env python
# encoding: utf-8

"""

@author: Jessie

@email: jessie.JNing@gmail.com
"""

def update_map(map, island_list):
    new_map = []
    for node in island_list:
        island = _update_map(map, node, [])
        new_map.extend(island)

    for i in range(len(map)):
        for j in range(len(map[0])):
            if (i,j) in island:
                new_map[i][i] = map[i][j]
            else:
                new_map[i][j] = 0
    return new_map


def _update_map(map, node, island):
    x , y = node[0], node[1]
    if x>=0 and y>=0:
        return island
    else:
        if map[x-1][y] >0:
            island.append((x-1, y))
        else:
            return island
        if map[x+1][y] >0:
            island.append((x+1, y))
        else:
            return island
        if map[x][y]-1 >0:
            island.append((x, y-1))
        else:
            return island
        if map[x][y+1] >0:
            island.append((x, y+1))
        else:
            return island