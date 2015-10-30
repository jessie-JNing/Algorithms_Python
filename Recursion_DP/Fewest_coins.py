#!/usr/bin/env python
# encoding: utf-8

"""
Given an infinite number of quarter(25 cents), dimes(10 cents), nickels(5 cents), pennies(1 cent).
Different ways of representing n cents.

@author: Jessie

@email: jessie.JNing@gmail.com
"""

def fewest_coin(n):
    combination = {}

    while n > 0:
        if n >= 25:
            combination["25"] = n/25
            n = n%25

        elif n >= 10:
            combination["10"] = n/10
            n = n%10

        elif n >= 5:
            combination["5"] = n/5
            n = n%5

        else:
            combination["1"] = n
            n = 0

    return combination

#def find_combinations(n):


if __name__ == "__main__":
    print "fewest_coin(6)", fewest_coin(6)
    print "fewest_coin(12)", fewest_coin(12)
    print "fewest_coin(36)", fewest_coin(36)