#!/bin/python3

import math
import os
import random
import re
import sys
import operator

import json
from pprint import pprint


def print_all_values(data, value):
    print(data)
    is_list = isinstance(data, list)
    if isinstance(data, dict):
        if 'red' in data:
            return value
        if 'red' in data.values():
            return value
        for _item in data.values():
            print(_item)
            value = print_all_values(_item, value)
    if isinstance(data, list):
        for _item in data:
            print(_item)
            value = print_all_values(_item, value)

    # else:
    else:  # print(item)
        if isinstance(data, int):
            value = value + data
            return value
    return value


if __name__ == '__main__':
    print("Day 12: https://adventofcode.com/2015/day/12")

    with open('input.json') as f:
        data = json.load(f)

        test = json.loads('{"a":{"b":4},"c":-1} ')
        # list.__iter__()
        print(print_all_values(test, 0))
        print(print_all_values(json.loads('[-1,{"a":1}]'), 0))
        print(print_all_values(json.loads('{"d":"red","e":[1,2,3,4],"f":5}'), 0))

        # Part One
        print(print_all_values(data, 0))
        # pprint(data)
