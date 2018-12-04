#!/bin/python3

from collections import namedtuple

_Aunt = namedtuple("Aunt",
                   ["children", "cats", "samoyeds", "pomeranians", "akitas", "vizlas", "goldfish", "trees", "cars",
                    "perfumes"])


class Aunt:
    def __init__(self):
        self.children = ''
        self.cats = ''
        self.samoyeds = ''
        self.akitas = ''
        self.cars = ''
        self.trees = ''
        self.goldfish = ''
        self.vizslas = ''
        self.pomeranians = ''
        self.perfumes = ''


def do_it(_data):
    aunts = {}
    controller = set()
    for line in _data:
        aunt = Aunt()
        items = line.replace(':', '').replace(',', '').split(' ')
        if 'children' in items:
            aunt.children = items[items.index('children') + 1]
        if 'cats' in items:
            aunt.cats = items[items.index('cats') + 1]
        if 'samoyeds' in items:
            aunt.samoyeds = items[items.index('samoyeds') + 1]
        if 'pomeranians' in items:
            aunt.pomeranians = items[items.index('pomeranians') + 1]
        if 'akitas' in items:
            aunt.akitas = items[items.index('akitas') + 1]
        if 'vizslas' in items:
            aunt.vizslas = items[items.index('vizslas') + 1]
        if 'goldfish' in items:
            aunt.goldfish = items[items.index('goldfish') + 1]
        if 'trees' in items:
            aunt.trees = items[items.index('trees') + 1]
        if 'cars' in items:
            aunt.cars = items[items.index('cars') + 1]
        if 'perfumes' in items:
            aunt.perfumes = items[items.index('perfumes') + 1]
        aunts[items[1]] = aunt
        controller.add(items[1])
    aunt_data = Aunt()
    aunt_data.children = '3'
    aunt_data.cats = '7'
    aunt_data.perfumes = '1'
    aunt_data.cars = '2'
    aunt_data.trees = '3'
    aunt_data.goldfish = '5'
    aunt_data.vizslas = '0'
    aunt_data.pomeranians = '3'
    aunt_data.akitas = '0'
    aunt_data.samoyeds = '2'

    for _aunt in aunts:
        if aunts[_aunt].children != '' and aunts[_aunt].children != aunt_data.children:
            controller.remove(_aunt)
            continue
        if aunts[_aunt].cats != '' and int(aunts[_aunt].cats) <= int(aunt_data.cats):
            controller.remove(_aunt)
            continue
        if aunts[_aunt].perfumes != '' and aunts[_aunt].perfumes != aunt_data.perfumes:
            controller.remove(_aunt)
            continue
        if aunts[_aunt].cars != '' and aunts[_aunt].cars != aunt_data.cars:
            controller.remove(_aunt)
            continue
        if aunts[_aunt].trees != '' and int(aunts[_aunt].trees) <= int(aunt_data.trees):
            controller.remove(_aunt)
            continue
        if aunts[_aunt].pomeranians != '' and int(aunts[_aunt].pomeranians) >= int(aunt_data.pomeranians):
            controller.remove(_aunt)
            continue
        if aunts[_aunt].akitas != '' and aunts[_aunt].akitas != aunt_data.akitas:
            controller.remove(_aunt)
            continue
        if aunts[_aunt].samoyeds != '' and aunts[_aunt].samoyeds != aunt_data.samoyeds:
            controller.remove(_aunt)
            continue
        if aunts[_aunt].goldfish != '' and int(aunts[_aunt].goldfish) >= int(aunt_data.goldfish):
            controller.remove(_aunt)
            continue
        if aunts[_aunt].vizslas != '' and aunts[_aunt].vizslas != aunt_data.vizslas:
            controller.remove(_aunt)

    print(controller)


if __name__ == '__main__':
    print("Day 16: https://adventofcode.com/2015/day/16")

    file = open("input.txt", 'r')
    data = file.read().split('\n')

    do_it(data)
