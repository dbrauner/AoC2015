#!/bin/python3

import sys


def calculate_score(ingredients, items):
    capacity = 0
    for counter, value in enumerate(ingredients):
        capacity += items[counter] * ingredients[value][0]
    durability = 0
    for counter, value in enumerate(ingredients):
        durability += items[counter] * ingredients[value][1]
    flavor = 0
    for counter, value in enumerate(ingredients):
        flavor += items[counter] * ingredients[value][2]
    texture = 0
    for counter, value in enumerate(ingredients):
        texture += items[counter] * ingredients[value][3]
    if capacity < 0:
        capacity = 0
    if durability < 0:
        durability = 0
    if flavor < 0:
        flavor = 0
    if texture < 0:
        texture = 0
    # Part Two -> comment from here
    calories = 0
    for counter, value in enumerate(ingredients):
        calories += items[counter] * ingredients[value][4]
    if calories != 500:
        return 0
    # Part Two -> to here
    return capacity * durability * flavor * texture


def do_it(data):
    ingredients = {}
    for line in data:
        ingredient, _cap, capacity, _dur, durability, _fla, flavor, _text, texture, _k, calories = line. \
            replace(':', '').replace(',', '').split(' ')
        capacity, durability, flavor, texture, calories = int(capacity), int(durability), \
                                                          int(flavor), int(texture), int(calories)
        ingredients[ingredient] = [capacity, durability, flavor, texture, calories]

    items = [100, 0, 0, 0]
    max_score = 0
    while True:

        score = calculate_score(ingredients, items)
        if score > max_score:
            max_score = score

        items[0] -= 1
        items[1] += 1
        if items[1] == 99:
            items[2] += 1
            items[1] = 0
            items[0] = 100 - items[2] - items[3]
        if items[2] == 99:
            items[3] += 1
            items[2] = 0
            items[1] = 0
            items[0] = 100 - items[2] - items[3]
        if items[3] == 99:
            break

    print(max_score)


if __name__ == '__main__':
    print("Day 15: https://adventofcode.com/2015/day/15")

    file = open("input.txt", 'r')
    data = file.read().split('\n')

    test_input = ['Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
                  'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3']

    do_it(data)
