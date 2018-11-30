#!/bin/python3

import math
import os
import random
import re
import sys
import operator


def count_code_space(line):
    dq = False
    escape = False
    wc = 0
    chars = 0
    hex = False
    for c in line:
        if hex:
            chars += 1
            if chars == 2:
                wc += 1
                chars = 0
                hex = False
            continue
        if escape:
            if c == 'x':
                hex = True
            if c == '"' or c == '\\':
                wc += 1
            escape = False
            continue
        if c == '\\':
            escape = True
            continue
        if c != '"':
            wc += 1
    return wc


def count_encoded_space(line):
    dq = False
    escape = False
    wc = 0
    chars = 0
    hex = False
    for c in line:
        # if hex:
        #     chars += 1
        #     if chars == 2:
        #         wc += 1
        #         chars = 0
        #         hex = False
        #     continue
        if escape:
            # # if c == 'x':
            # #     hex = True
            # if c == '"' or c == '\\':
            wc += 1
            escape = False
            continue
        if c == '\\':
            # escape = True
            wc += 2
            continue
        if c != '"':
            wc += 1
        else:
            wc += 2
    wc += 2
    print("line: " + line + " was " + str(wc))
    return wc


def count_space(arr):
    space = 0
    for line in arr:
        space += len(line) - count_code_space(line)
    return space


def invert_count_space(arr):
    space = 0
    for line in arr:
        space += count_encoded_space(line) - len(line)
    return space


if __name__ == '__main__':
    print("Day 8: https://adventofcode.com/2015/day/8")
    file = open("input.txt", 'r')

    input = file.read().split('\n')
    test_input = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']
    print(count_space(test_input))

    # Part One
    print(count_space(input))

    print(invert_count_space(test_input))

    print(invert_count_space(input))

