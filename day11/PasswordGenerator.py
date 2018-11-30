#!/bin/python3

import math
import os
import random
import re
import sys
import operator


def has_sequence(pwd):
    last = pwd[0]
    seq = 1

    for c in pwd:
        if chr(ord(c) - 1) == last:
            seq += 1
        else:
            seq = 1
        last = c
        if seq == 3:
            return True
    return False


def has_two_pairs(pwd):
    pairs = set()

    last = ''

    for c in pwd:
        if c == last:
            pairs.add(c)
        last = c
    return len(pairs) >= 2


def check_password(pwd):
    if str(pwd).__contains__('i') or str(pwd).__contains__('o') or str(pwd).__contains__('l'):
        return False
    if not has_sequence(pwd):
        return False
    return has_two_pairs(pwd)


def update_by_index(pwd, index):
    if pwd[index] == 'z':
        _list = list(pwd)
        _list[index] = 'a'
        pwd = ''.join(_list)

        pwd = update_by_index(pwd, index - 1)
        return pwd

    x = pwd[index]
    x = chr(ord(x) + 1)

    _list = list(pwd)
    _list[index] = x
    pwd = ''.join(_list)
    return pwd


def next_password(pwd):
    compliant = False

    while not compliant:
        pwd = update_by_index(pwd, 7)
        compliant = check_password(pwd)

    return pwd


if __name__ == '__main__':
    print("Day 11: https://adventofcode.com/2015/day/11")

    print(next_password('abcdefgh'))
    print(next_password('ghijklmn'))

    # Part One
    print(next_password('cqjxjnds'))

    # Part Two
    print(next_password('cqjxxyzz'))
