#!/bin/python3

import math
import os
import random
import re
import sys
import hashlib


def findHash(secret, zeros):
    m = hashlib.md5()
    initial = '000000'
    for i in range(sys.maxsize):
        value = hashlib.md5((secret + str(i)).encode('utf-8')).hexdigest()
        # print(value)
        if value[0:zeros] == initial[0:zeros]:
            print("for value: " + str(i) + " the hash was: " + value)
            return


if __name__ == '__main__':
    print("Day 4: https://adventofcode.com/2015/day/4")
    # Part One
    findHash('iwrupvqb', 5)
    # Part Two
    findHash('iwrupvqb', 6)
