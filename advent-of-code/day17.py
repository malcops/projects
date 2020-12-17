#!/usr/bin/env python3
from day11 import pad_2d_with_floor
import pytest

input_list = []
with open('day17.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append([x for x in item])

# if cube is active, and 2-3 neighbors are active -> cube remains active
# if cube is inactive, but 3 neighbors are active -> cube becomes active

example1 = [['.','#','.'],
            ['.','.','#'],
            ['#','#','#']]

def print_2d(array_2d):
    print(array_2d)
    for line in array_2d:
        print ("".join(line))
    print("")

def process_cube(array_3d):

    assert len(array_3d) == len(array_3d[0]) == len(array_3d[0][0])
    assert len(array_3d) >= 5
    new_cube = array_3d[:]
    valid_dim = list(range(1,len(array_3d)-1))
    print(len(array_3d))
    print(valid_dim)
    print(array_3d)
    for zidx, z in enumerate(array_3d):
        for yidx, y in enumerate(z):
            for xidx, x, in enumerate(y):
                if not all(idx in valid_dim for idx in [xidx, yidx, zidx]):
                    pass
                else:
                    count = 0
                    slice_before = [i[xidx-1:xidx+2] for i in array_3d[zidx-1][yidx-1:yidx+2]]
                    slice_before_count = sum([i.count("#") for i in slice_before])
                    this_slice = [i[xidx-1:xidx+2] for i in array_3d[zidx][yidx-1:yidx+2]]
                    this_slice[1][1] = '.' # ignore current spot
                    this_slice_count = sum([i.count("#") for i in this_slice])
                    slice_after = [i[xidx-1:xidx+2] for i in array_3d[zidx+1][yidx-1:yidx+2]]
                    slice_after_count = sum([i.count("#") for i in slice_after])
                    count = slice_before_count + this_slice_count + slice_after_count
                    assert len(slice_before) == 3
                    assert len(slice_before[0]) == 3
                    assert len(this_slice) == 3
                    assert len(this_slice[0]) == 3
                    assert len(slice_after) == 3
                    assert len(slice_after[0]) == 3
                    print(x, xidx, yidx, zidx)
                    print(sum([q.count("#") for q in slice_before]))
                    print_2d(slice_before)

    return new_cube



example1_padded = [[['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.']],
                   [['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.']],
                   [['.', '.', '.', '.', '.'], # z=0
                    ['.', '.', '#', '.', '.'],
                    ['.', '.', '.', '#', '.'],
                    ['.', '#', '#', '#', '.'],
                    ['.', '.', '.', '.', '.']],
                   [['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.']],
                   [['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.']]]

example2_padded = [[['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.']],
                   [['.', '.', '.', '.', '.'], # z=-1
                    ['.', '#', '.', '.', '.'],
                    ['.', '.', '.', '#', '.'],
                    ['.', '.', '#', '.', '.'],
                    ['.', '.', '.', '.', '.']],
                   [['.', '.', '.', '.', '.'], # z=0
                    ['.', '#', '.', '#', '.'],
                    ['.', '.', '#', '#', '.'],
                    ['.', '.', '#', '.', '.'],
                    ['.', '.', '.', '.', '.']],
                   [['.', '.', '.', '.', '.'], #z=1
                    ['.', '.', '#', '.', '.'],
                    ['.', '.', '.', '#', '.'],
                    ['.', '#', '#', '#', '.'],
                    ['.', '.', '.', '.', '.']],
                   [['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.']]]
def test_process_cube():

    processed = process_cube(example1_padded)
    assert processed == example2_padded



def test_part_one():

    array_3d = part_one(example1)
    assert array_3d[0][0][0] == '.'
    assert array_3d[2][:][:] == pad_2d_with_floor(example1)
    assert array_3d[2][4][4] == '.'




def part_one(input_list):

    # "floor" from day11 is '.'
    array = pad_2d_with_floor(input_list)
    x_dim = len(array[0])
    y_dim = len(array)
    new_slice = [['.']*x_dim for x in range(y_dim)]
    array_3d = [new_slice, new_slice, array, new_slice, new_slice]

    # assert it's a cube
    assert len(array_3d) == len(array_3d[0]) == len(array_3d[0][0])

    process_cube(array_3d)
    print(array_3d)
    return array_3d


def part_two(input_list):

    pass


if __name__ == "__main__":

    part_one(example1)
    part_two(input_list)
