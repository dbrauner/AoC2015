#!/bin/python3

import math
import os
import random
import re
import sys


def countLights(instructions):
    lightsOn = 0
    # grid = [1000][1000]
    lights = {}
    for instruction in instructions:
        command = instruction.split(' ')
        if command[0] == 'turn':
            if command[1] == 'on':
                op = 'on'
            else:
                op = 'off'
            xIni, yIni = map(int, (command[2].split(',')))
            xFin, yFin = map(int, (command[4].split(',')))
        else:
            op = 'tog'
            xIni, yIni = map(int, (command[1].split(',')))
            xFin, yFin = map(int, (command[3].split(',')))

        for i in range(xIni, xFin + 1):
            for j in range(yIni, yFin + 1):
                key = str(i) + ',' + str(j)
                if op == 'on':
                    lights[key] = 'x'
                else:
                    if op == 'off':
                        lights[key] = ' '
                if op == 'tog':
                    if key in lights:
                        if lights[key] == 'x':
                            lights[key] = ' '
                        else:
                            lights[key] = 'x'
                    else:
                        lights[key] = 'x'
    lightedOn = {k: v for k, v in lights.items() if v == 'x'}

    return len(lightedOn)


def countDimedLights(instructions):
    lights = {}
    for instruction in instructions:
        print(instruction)
        command = instruction.split(' ')
        if command[0] == 'turn':
            if command[1] == 'on':
                op = 'on'
            else:
                op = 'off'
            xIni, yIni = map(int, (command[2].split(',')))
            xFin, yFin = map(int, (command[4].split(',')))
        else:
            op = 'tog'
            xIni, yIni = map(int, (command[1].split(',')))
            xFin, yFin = map(int, (command[3].split(',')))

        for i in range(xIni, xFin + 1):
            for j in range(yIni, yFin + 1):
                key = str(i) + ',' + str(j)
                if key not in lights:
                    lights[key] = 0

                if op == 'on':
                    lights[key] += 1
                if op == 'off':
                    if lights[key] > 0:
                        lights[key] -= 1
                if op == 'tog':
                    lights[key] += 2
    lightedOn = sum(lights.values())

    return lightedOn


if __name__ == '__main__':
    print("Day 6: https://adventofcode.com/2015/day/6")
    file = open("input.txt", 'r')

    input = file.read().split('\n')

    print(countLights({'toggle 0,0 through 999,0'}))
    print(countLights({'turn on 0,0 through 999,999'}))
    # Part One
    # print(countLights(input))

    print(countDimedLights(input))
