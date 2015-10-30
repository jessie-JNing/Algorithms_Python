#!/usr/bin/env python
# encoding: utf-8

"""
Imagine a robot sitting on the upper left corner of a X by Y grid.
The robot can only move in two directions: right and down.
How many possible path are thre for the robot to go
from (0,0) to (X, Y)?

FOLLOW UP:
Imagine certain spots are "off limits", such that the robot can not
step on them. Desgin an algorithm to find a path for the robot from
from the top left to bottom right.

@author: Jessie

@email: jessie.JNing@gmail.com

"""

def robot_move(x, y):
    if x == 0 and y == 0:
        return 0
    if x == 0 and y > 0:
        return 1
    if x > 0 and y == 0:
        return 1
    else:
        return robot_move(x-1, y-1) + 2

if __name__=="__main__":
    print "robot_move(2, 2)", robot_move(2, 2)