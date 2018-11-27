#!/bin/python3

import math
import os
import random
import re
import sys


def containVowels(word):
    vowels = 0

    for c in word:
        if c in {'a', 'e', 'i', 'o', 'u'}:
            vowels += 1

        if vowels >= 3:
            return True
    return False


def containTwiceInRow(word):
    last = ' '
    for c in word:
        if c == last:
            return True
        last = c
    return False


def isNotUglySequence(word):
    if 'ab' in word:
        return False
    if 'cd' in word:
        return False
    if 'pq' in word:
        return False
    if 'xy' in word:
        return False
    return True


def findNiceStrings(arr):
    niceWords = 0
    for word in arr:
        if containVowels(word) and containTwiceInRow(word) and isNotUglySequence(word):
            niceWords += 1
    return niceWords


def containsPair(word):
    for i in range(len(word) - 2):
        if word[i:i+2] in word[i + 2:]:
            print(word[i:i + 2] + ' and ' + word[i + 2:])
            return True
    return False


def containsRepeated(word):
    for i in range(len(word) - 2):
        if word[i] == word[i + 2]:
            return True
    return False


def findReallyNiceString(arr):
    niceWords = 0
    for word in arr:
        if containsPair(word) and containsRepeated(word):
            niceWords += 1
    return niceWords


if __name__ == '__main__':
    print("Day 5: https://adventofcode.com/2015/day/5")
    file = open("input.txt", 'r')

    findNiceStrings({'ugknbfddgicrmopn'})

    findNiceStrings({'aaa'})

    findNiceStrings({'jchzalrnumimnmhp'})

    findNiceStrings({'haegwjzuvuyypxyu'})

    findNiceStrings({'dvszwmarrgswjxmb'})
    input = file.read().split('\n')

    # Part One
    print(findNiceStrings(input))

    findReallyNiceString({'qjhvhtzxzqqjkmpb'})

    findReallyNiceString({'xxyxx'})

    findReallyNiceString({'uurcxstgmygtbstg'})

    findReallyNiceString({'ieodomkazucvgmuy'})

    # Part Two
    print(findReallyNiceString(input))

