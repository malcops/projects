#!/usr/bin/env python3
import numpy as np
import pytest
import time

foods = []
with open('day21.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            foods.append(item)

print(foods)

def part_one(input_list):
    pass

def part_two(input_list):
    pass


if __name__ == "__main__":

    start = time.time()
    part_one(foods)
    stop = time.time()
    print("time: ", stop - start)

    start = time.time()
    part_two(foods)
    stop = time.time()
    print("time: ", stop - start)