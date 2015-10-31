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
import random

def isFree(x, y):
    #return True if random.randint(0, 1)==1 else False
    return True

def robot_move(x, y):
    if x > y:
        return robot_move(y, x)
    else:
        numerator = 1
        denominator = 1
        for i in range(x):
            numerator *= (x + y -i)
            denominator *= (x - i)
        return numerator/denominator

# find out the path in maze with stuck
def find_path(x, y, path):
    path.append((x, y))
    if x==0 and y == 0:
        return True

    success = False
    if x >0 and isFree(x-1, y):
        success = find_path(x-1, y, path)

    if not success and y>0 and isFree(x, y-1):
        success = find_path(x, y-1, path)

    if success:
        path.append((x, y))
    return success



if __name__=="__main__":
    print "robot_move(2, 2)", find_path(10, 4, [])