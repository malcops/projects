#!/usr/bin/env python3
import pytest


def part_one(input_list):

    working = input_list[:]

    idx = len(input_list) + 1
    while idx < 2018:
        last = working[-1]
        if working.count(last) <= 1:
            working.append(0)
        else:
            previous_index = 0
            for idx, val in enumerate(working[:-1]):
                if working[idx] == last:
                    previous_index = idx
            last_index = len(working) - 1
            working.append(last_index - previous_index)
        idx += 1

    print(working[-1])
    return working[-1]


def part_two(input_list):

    pass


if __name__ == "__main__":

    example1 = [0,3,6]
    example2 = [1,3,2]
    example3 = [2,1,3]
    example4 = [1,2,3]
    example5 = [2,3,1]
    example6 = [3,2,1]
    example7 = [3,1,2]
    input_list = [0,8,15,2,12,1,4]

    assert part_one(example1) == 436
    assert part_one(example2) == 1
    assert part_one(example3) == 10
    assert part_one(example4) == 27
    assert part_one(example5) == 78
    assert part_one(example6) == 438
    assert part_one(example7) == 1836
    part_one(input_list)
    part_two(input_list)
