#!/bin/python3

import math
import os
import random
import re
import sys


def calculateOrder(arr):
    order = 0
    ribbon = 0
    for line in arr:
        order += wrappingPaper(line) + slackSize(line)
        ribbon += ribbonSize(line)

    print("Part Two: " + str(ribbon) + " feet of ribbon needed")
    return order


def wrappingPaper(line):
    l, w, h = map(int, line.split('x'))

    wrap = 2 * l * w + 2 * w * h + 2 * h * l
    return wrap


def slackSize(line):
    dimensions = list(map(int, line.split('x')))
    dimensions.sort()

    slack = dimensions[0] * dimensions[1]
    return slack


def ribbonSize(line):
    dimensions = list(map(int, line.split('x')))
    dimensions.sort()

    wrap = (dimensions[0] * 2) + (dimensions[1] * 2)
    bow = dimensions[0] * dimensions[1] * dimensions[2]
    return wrap + bow


if __name__ == '__main__':
    print("Day 2: https://adventofcode.com/2015/day/2")
    file = open("input.txt", 'r')
    input = file.read()

    print(calculateOrder(input.split('\n')))
