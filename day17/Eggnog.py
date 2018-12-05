#!/bin/python3

import sys

MAX_SIZE = 150


def check_capacity(containers, max_quantity, same_quantity):
    total, quantity = 0, 0
    for c in containers:
        if c[1] == 1:
            total += c[0]
            quantity += 1
    if total == MAX_SIZE:
        if quantity < max_quantity:
            max_quantity = quantity
            same_quantity = 0
        if quantity == max_quantity:
            return [True, quantity, same_quantity + 1]
        return [True, max_quantity, same_quantity]
    return [False, 0]


def do_it(_data):
    containers = list(map(int, _data))
    print(containers)
    containers.sort()
    _containers = [[i, 0] for i in containers]

    combination, same_quantity = 0, 0
    quantity = sys.maxsize
    while True:
        first = _containers[0]
        first[1] += 1
        rest = False
        for el in _containers:
            if rest:
                rest = False
                el[1] += 1
            if el[1] == 2:
                rest = True
                el[1] = 0
                continue
        all_one = True
        for el in _containers:
            if el[1] == 0:
                all_one = False

        result = check_capacity(_containers, quantity, same_quantity)
        if result[0]:
            combination += 1
            quantity = result[1]
            same_quantity = result[2]

        if all_one:
            break

    print('Part One', combination)
    print('Part Two', same_quantity)


if __name__ == '__main__':
    print("Day 17: https://adventofcode.com/2015/day/17")

    file = open("input.txt", 'r')
    data = file.read().split('\n')

    # test_input = ['20', '15', '10', '5', '5']
    # do_it(test_input)

    do_it(data)
