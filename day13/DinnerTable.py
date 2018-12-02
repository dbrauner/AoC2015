#!/bin/python3

import sys

happiness = {}
family = set()
already_sit = set()
last = ''


def find_best_neighbor(i):
    level = - sys.maxsize - 1
    for _i in family:
        if _i not in already_sit and _i != i:
            if happiness[(i, _i)] + happiness[(_i, i)] > level:
                _next = _i
                level = happiness[(i, _i)]
    return _next


def calculate_happiness(i):
    if len(already_sit) == len(family):
        return 0
    _next = find_best_neighbor(i)
    already_sit.add(_next)
    global last
    last = _next
    return calculate_happiness(_next) + happiness[(i, _next)] + happiness[(_next, i)]


def find_optimal_arrangement(data, part_two):
    happiness.clear()
    already_sit.clear()
    family.clear()
    arrangements = set()
    for line in data:
        a, would, level, amount, _h, _units, _by, _sitting, _next, _to, b = line.split(' ')
        amount = int(amount)
        b = b.replace('.', '')

        happiness[(a, b)] = amount if level == 'gain' else 0 - amount
        if part_two:
            happiness[(a, 'Doug')] = 0
            happiness[('Doug', a)] = 0
            family.add('Doug')
        family.add(a)
    for i in family:
        already_sit.clear()
        already_sit.add(i)
        happy_amount = calculate_happiness(i) + happiness[(i, last)] + happiness[(last, i)]
        arrangements.add(happy_amount)
    print(max(arrangements))


if __name__ == '__main__':
    print("Day 13: https://adventofcode.com/2015/day/13")

    file = open("test_input.txt", 'r')

    test_input = file.read().split('\n')
    find_optimal_arrangement(test_input, False)

    # Part One
    file = open("input.txt", 'r')
    part_one_input = file.read().split('\n')
    find_optimal_arrangement(part_one_input, False)

    # Part Two
    find_optimal_arrangement(part_one_input, True)
