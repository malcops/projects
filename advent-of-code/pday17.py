#!/usr/bin/env python3
import numpy as np
import pytest

example1 = [[0,1,0],
            [0,0,1],
            [1,1,1]]

input1 = [
[0,0,0,1,0,0,1,0],
[0,0,1,1,0,1,1,0],
[0,0,1,0,0,0,0,0],
[0,0,0,0,1,0,0,0],
[1,0,1,1,0,0,0,1],
[1,1,1,1,0,0,1,1],
[0,0,0,1,1,0,1,0],
[1,0,1,0,1,0,0,0]]


def process_cube(cube):
    
    print(len(cube))
    start = 0
    stop = len(cube)
    new_cube = np.copy(cube)
    print(new_cube)
    for x in range(start, stop):
        for y in range (start, stop):
            for z in range(start, stop):
                if cube[x][y][z]:
                    print(x,y,z)
                    count = np.count_nonzero(cube[x-1:x+2, y-1:y+2, z-1:z+2]) # for the current cube
                    print(count-1)
                    if count-1 not in (2,3):
                        print('active next cycle = false')
                        new_cube[x][y][z] = 0
                else:
                    count = np.count_nonzero(cube[x-1:x+2, y-1:y+2, z-1:z+2])
                    if count == 3:
                        print("going active",x,z,y)
                        new_cube[x][y][z] = 1
    
    return new_cube



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
    return np.pad(array, 1, mode='constant')


def part_one(input_list):
    a = np.array(input_list, ndmin=3)
    a_slice = np.full_like(a, fill_value=0)
    start_array = np.concatenate([a_slice, a, a_slice], 0)
    print(start_array.shape)
    start_array = grow_by_one(start_array)
    start_array = process_cube(start_array)
    it = 1
    while it != 6:
        start_array = grow_by_one(start_array)
        start_array = process_cube(start_array)
        it += 1  
    count = np.count_nonzero(start_array)
    print("Part1: ", count)
    # 153 - too low
    return count


def part_two(input_list):

    pass


if __name__ == "__main__":

    # part_one(example1)
    part_one(input1)
    part_two(input1)
