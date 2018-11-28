#!/bin/python3

import math
import os
import random
import re
import sys
import operator
from collections import defaultdict

signals = defaultdict(lambda: None)


def bitwiseComplement(param):
    current = signals[param]
    if current is not None:
        return ~current


def bitwiseAND(param, param1):
    a, b = signals[param], signals[param1]
    if str.isnumeric(param):
        a = int(param)
    if str.isnumeric(param1):
        b = int(param1)
    if a is not None and b is not None:
        return a & b


def bitwiseOR(param, param1):
    a, b = signals[param], signals[param1]
    if str.isnumeric(param):
        a = int(param)
    if str.isnumeric(param1):
        b = int(param1)
    if a is not None and b is not None:
        return a | b


def bitwiseLSHIFT(param, param1):
    a, b = signals[param], int(param1)
    if a is not None:
        return a << b


def bitwiseRSHIFT(param, param1):
    a, b = signals[param], int(param1)
    if a is not None:
        return a >> b


def executeInstruction(instruction):
    if instruction[0] == 'NOT':
        signals[instruction[3]] = bitwiseComplement(instruction[1])
        return
    if instruction[1] == 'AND':
        signals[instruction[4]] = bitwiseAND(instruction[0], instruction[2])
        return
    if instruction[1] == 'OR':
        signals[instruction[4]] = bitwiseOR(instruction[0], instruction[2])
        return
    if instruction[1] == 'LSHIFT':
        signals[instruction[4]] = bitwiseLSHIFT(instruction[0], instruction[2])
        return
    if instruction[1] == 'RSHIFT':
        signals[instruction[4]] = bitwiseRSHIFT(instruction[0], instruction[2])
        return
    if str.isnumeric(instruction[0]) and instruction[1] == '->':
        signals[instruction[2]] = int(instruction[0])
        return
    if signals[instruction[0]] is not None:
        signals[instruction[2]] = signals[instruction[0]]


def assembleWires(arr):
    while not signals['a']:
        for item in arr:
            instruction = item.split(' ')
            executeInstruction(instruction)


if __name__ == '__main__':
    print("Day 7: https://adventofcode.com/2015/day/7")
    file = open("input.txt", 'r')

    input = file.read().split('\n')

    # Test case 1
    arr_test = ["123 -> x", "456 -> y", "x AND y -> d", "x OR y -> e", "x LSHIFT 2 -> f", "y RSHIFT 2 -> g",
                "NOT x -> h", "NOT y -> i"]

    # assembleWires(arr_test)

    assembleWires(input)

    print(signals)

    print(signals['a'])
