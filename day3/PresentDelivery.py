#!/bin/python3

import math
import os
import random
import re
import sys

from collections import namedtuple

MyThingBase = namedtuple("MyThingBase", ["line", "column"])


class House(MyThingBase):
    def __new__(cls, line, column):
        obj = MyThingBase.__new__(cls, line, column)
        return obj


def calculateRepeatedHouses(moves):
    houses = {}
    x, y = 0, 0
    first = House(0, 0)
    houses[first] = 1
    for m in moves:
        if m == '^':
            y += 1
        if m == '>':
            x += 1
        if m == 'v':
            y -= 1
        if m == '<':
            x -= 1

        house = House(x, y)
        if house in houses:
            if houses[house] == 1:
                houses[house] += 1
        else:
            houses[house] = 1

    return len(houses)

def RobotSanta(moves):
    houses = {}
    xSanta, ySanta = 0, 0
    xRobot, yRobot = 0, 0
    first = House(0, 0)
    houses[first] = 1
    santa = True
    for m in moves:
        if santa:
            if m == '^':
                ySanta += 1
            if m == '>':
                xSanta += 1
            if m == 'v':
                ySanta -= 1
            if m == '<':
                xSanta -= 1
            house = House(xSanta, ySanta)
            santa = False
        else:
            if m == '^':
                yRobot += 1
            if m == '>':
                xRobot += 1
            if m == 'v':
                yRobot -= 1
            if m == '<':
                xRobot -= 1
            house = House(xRobot, yRobot)
            santa = True
        if house in houses:
            if houses[house] == 1:
                houses[house] += 1
        else:
            houses[house] = 1

    return len(houses)

if __name__ == '__main__':
    print("Day 3: https://adventofcode.com/2015/day/3")
    file = open("input.txt", 'r')
    input = file.read()
    calculateRepeatedHouses('^>v<')
    print(calculateRepeatedHouses(input))
    print(RobotSanta(input))
