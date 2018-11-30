#!/bin/python3

import math
import os
import random
import re
import sys
import operator


def play_game(seq, times):

    for _ in range(times):

        last = seq[0]
        times = 0
        new_seq = ''
        for c in seq:
            if c == last:
                times += 1
            else:
                new_seq += str(times) + last
                last = c
                times = 1
        new_seq += str(times) + last
        seq = new_seq
        # print(new_seq)
    return len(new_seq)


if __name__ == '__main__':
    print("Day 10: https://adventofcode.com/2015/day/10")

    # Test Part
    print(play_game('1', 1))
    print(play_game('11', 1))
    print(play_game('21', 1))
    print(play_game('1211', 1))
    print(play_game('111221', 1))

    # Part One
    print(play_game('1113122113', 40))

    # Part Two
    print(play_game('1113122113', 50))
