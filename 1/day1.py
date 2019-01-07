#!/usr/bin/env python
# day1.py - aoc 2018 day 1 solutions
# Copyright 2019 Jillian A. Bolton, All Rights Reserved

def drift(deltas):
    freq = 0

    for d in deltas.splitlines():
        freq += int(d)

    return freq

if __name__ == "__main__":

    file = open('input')
    deltas = file.read().strip()
    file.close()

    freq = drift(deltas)
    print('freq ', freq)
