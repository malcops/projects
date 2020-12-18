#!/usr/bin/env python3
import numpy as np
import pytest

input_list = []
with open('day17.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(item)

example1 = [['.','#','.'],
            ['.',',','#'],
            ['#','#','#']]

@pytest.mark.parametrize("input_array, output_dimensions", [
                         (np.full((3,3,3), 1), (5,5,5)),
                         ])
def test_grow_by_one(input_array, output_dimensions):

    output = grow_by_one(input_array)
    assert output.shape == output_dimensions
    assert output[0][0][0] == 0
    assert output[4][4][4] == 0
    assert output[1][1][1] == 1

def grow_by_one(array):
    size_tuple = tuple(x+2 for x in array.shape)
    bigger = np.full(size_tuple, fill_value='.')
    print(bigger.size)
    print(bigger.shape)
    #bigger[1:-1][1:-1][1:-1] = array
    return np.pad(array, 1, mode='constant')

def part_one(input_list):
    a = np.array(input_list, ndmin=3)
    a_slice = np.full_like(a, fill_value=0)
    start_array = np.concatenate([a_slice, a, a_slice], 0)
    print(start_array.shape, start_array.size)
    return a


def part_two(input_list):

    pass

if __name__ == "__main__":

    part_one(example1)
    part_two(input_list)
