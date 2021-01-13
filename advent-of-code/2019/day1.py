#!/usr/bin/env python3
import pytest
import time

input_list = []
with open('day1.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(int(item))


@pytest.mark.parametrize("mass, fuel_required", [
                         (12, 2),
                         (14, 2),
                         (1969, 654),
                         (100756, 33583)
                         ])
def test_calculate_fuel(mass, fuel_required):

    assert fuel_required == calculate_fuel(mass)


def calculate_fuel(mass):

    return int(mass/3) - 2


def part_one(input_list):

    total = 0
    for mass in input_list:
        total += calculate_fuel(mass)
    print("Part 1: ", total)


@pytest.mark.parametrize("mass, fuel_required", [
                         (1969, 966),
                         (100756, 50346)
                         ])
def test_calculate_fuel_part2(mass, fuel_required):

    assert fuel_required == calculate_fuel_part2(mass)


def calculate_fuel_part2(mass):

    subtotal = mass
    total = 0
    while subtotal >= 0:
        subtotal = calculate_fuel(subtotal)
        if subtotal > 0:
            total += subtotal
    return total


def part_two(input_list):

    total = 0
    for mass in input_list:
        total += calculate_fuel_part2(mass)
    print("Part 2:", total)


if __name__ == "__main__":

    start = time.time()
    part_one(input_list)
    stop = time.time()
    print("time: ", stop - start)

    start = time.time()
    part_two(input_list)
    stop = time.time()
    print("time: ", stop - start)
