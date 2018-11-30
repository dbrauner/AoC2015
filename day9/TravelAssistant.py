#!/bin/python3

import math
import os
import random
import re
import sys
import operator
from collections import defaultdict

# visited = set()
def calculate_paths(city, path, weights, visited):
    try:
        _next = path.__next__()
        if _next == city:
            _next = path.__next__()
        if city in visited:
            _next = path.__next__()
            # return 0
        visited.add(city)
        # _next = next(path)
        # if _next is not None and _next != city:
        dist = weights.get((city, _next))
        print('peso ' + str(dist))
        return  calculate_paths(_next, path, weights, visited) + dist
    except StopIteration:
        return 0
        # print(name + " ->" + str(path[name]))
    #
    # for i in range(len(path)):
    #     x = list(path[i])
    #     print(x)
    #     print(path[i])
    # for city in path:
    #     # print(city.values)
    #     for _city in path[city]:
    #         print(city, _city)


def find_shortest_way(arr):
    weights = {}
    path = defaultdict(set)
    for line in arr:
        a, to, b, eq, distance = line.split(' ')
        weights[(a, b)] = int(distance)
        weights[(b, a)] = int(distance)

        path[a].add(b)
        path[b].add(a)

    _sum = list()
    for city in path:
        x = iter(path[city])
        for _city in path[city]:
            x = iter(path[city])
            _sum.append(calculate_paths(city, x, weights, set()))
            print(city, _city, _sum)

    print(path, weights)


if __name__ == '__main__':
    print("Day 9: https://adventofcode.com/2015/day/9")
    file = open("input.txt", 'r')

    input = file.read().split('\n')

    test_input = ["London to Dublin = 464", "London to Belfast = 518", "Dublin to Belfast = 141"]

    find_shortest_way(test_input)
