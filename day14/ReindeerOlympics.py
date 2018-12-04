#!/bin/python3

import sys


def calculate_distance(reindeer, race_time):
    x = int(race_time / (reindeer[1] + reindeer[2]))
    y = race_time % (reindeer[1] + reindeer[2])

    d = x * reindeer[1] * reindeer[0]
    if y <= reindeer[1]:
        d += y * reindeer[0]
    else:
        d += reindeer[0] * reindeer[1]
    return d


def create_reindeer_list(data):
    reindeers = {}
    for item in data:
        name, _can, _fly, speed, _kms, _for, time, _seconds, _but, _then, _must, _rest, _for, rest, _seconds = item.split(
            ' ')
        speed, time, rest = int(speed), int(time), int(rest)
        reindeers[name] = [speed, time, rest]
    return reindeers


def find_winners_distance(data):
    winner = 0
    reindeers = create_reindeer_list(data)
    for reindeer in reindeers:
        if calculate_distance(reindeers[reindeer], 2503) > winner:
            winner = calculate_distance(reindeers[reindeer], 2503)
    print(winner)


def find_winner_at_most_time(data):
    reindeers = create_reindeer_list(data)
    times_reinders = {}
    for i in range(1, 2503):
        rank = {}
        for reindeer in reindeers:
            distance = calculate_distance(reindeers[reindeer], i)
            rank[reindeer] = distance

        result = {k: v for k, v in rank.items() if v == max(rank.values())}
        for r in result:
            if r in times_reinders:
                times_reinders[r] += 1
            else:
                times_reinders[r] = 1
    print(max(times_reinders.values()))


if __name__ == '__main__':
    print("Day 13: https://adventofcode.com/2015/day/13")

    file = open("input.txt", 'r')
    data = file.read().split('\n')
    test_data = ['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
                 'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']

    find_winners_distance(data)

    find_winner_at_most_time(data)
