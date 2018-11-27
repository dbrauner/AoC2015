#!/bin/python3

import math
import os
import random
import re
import sys


def notQuiteLisp(input):
    floor = 0

    for i, c in enumerate(input):
        if c == '(':
            floor += 1
        else:
            floor -= 1
            if floor == -1:
                print("Entered the basement at position " +  str( i + 1))
    return floor


if __name__ == '__main__':
    print("Day 1: https://adventofcode.com/2015/day/1")
    file = open("input.txt", 'r')
    input = file.read()

    result = notQuiteLisp(input)

    print(str(result) + '\n')
