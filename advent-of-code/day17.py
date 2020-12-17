#!/usr/bin/env python3
from day11 import pad_2d_with_floor
import pytest

input_list = []
with open('day17.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append([x for x in item])

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
                    this_slice = [i[xidx-1:xidx+2] for i in array_3d[zidx][yidx-1:yidx+2]]
                    this_slice[1][1] = '.' # ignore current spot
                    slice_after = [i[xidx-1:xidx+2] for i in array_3d[zidx+1][yidx-1:yidx+2]]
                    assert len(slice_before) == 3
                    assert len(slice_before[0]) == 3
                    assert len(this_slice) == 3
                    assert len(this_slice[0]) == 3
                    assert len(slice_after) == 3
                    assert len(slice_after[0]) == 3
                    slice_before_count = sum([i.count("#") for i in slice_before])
                    this_slice_count = sum([i.count("#") for i in this_slice])
                    slice_after_count = sum([i.count("#") for i in slice_after])
                    count = slice_before_count + this_slice_count + slice_after_count

                    if (xidx, yidx, zidx) == (1,1,1):
                        print('1,1,1')
                        print_2d(slice_before)
                        print_2d(this_slice)
                        print_2d(slice_after)

                        print(count, slice_before_count, this_slice_count, slice_after_count)
                    # if cube is active, and 2-3 neighbors are active -> cube remains active
                    # if cube is inactive, but 3 neighbors are active -> cube becomes active
                    if x == '#' and count not in [2,3]:
                        # print('turn off cube')
                        new_cube[zidx][yidx][xidx] = '.'
                        # print(x, xidx, yidx, zidx)
                    if x == '.' and count == 3:
                        # print("turn on cube")
                        new_cube[zidx][yidx][xidx] = '#'
                        # print(x, xidx, yidx, zidx)

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


# this example input is completely fucked up
example2_padded = [[['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.']],
                   [['.', '.', '.', '.', '.'], # z=-1
                    ['.', '.', '.', '.', '.'],
                    ['.', '#', '.', '.', '.'],
                    ['.', '.', '.', '#', '.'],
                    ['.', '.', '#', '.', '.']],
                   [['.', '.', '.', '.', '.'], # z=0
                    ['.', '.', '.', '.', '.'],
                    ['.', '#', '.', '#', '.'],
                    ['.', '.', '#', '#', '.'],
                    ['.', '.', '#', '.', '.']],
                   [['.', '.', '.', '.', '.'], #z=1
                    ['.', '.', '.', '.', '.'],
                    ['.', '#', '.', '.', '.'],
                    ['.', '.', '.', '#', '.'],
                    ['.', '.', '#', '.', '.']],
                   [['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.']]]
def test_process_cube():

    processed = process_cube(example1_padded)
    for idx, layer in enumerate(processed):
        assert layer == example2_padded[idx]



def test_part_one():

    array_3d = part_one(example1)
    assert array_3d[0][0][0] == '.'
    assert array_3d[2][:][:] == pad_2d_with_floor(example1)
    assert array_3d[2][4][4] == '.'

array1 = [[['#']]]
array27 = [[['.', '.', '.'], ['.','.','.'], ['.','.','.']],
           [['.', '.', '.'], ['.','#','.'], ['.','.','.']],
           [['.', '.', '.'], ['.','.','.'], ['.','.','.']]]

array125 = [[['.','.','.', '.', '.'], ['.','.','.','.','.'], ['.','.','.','.','.'], ['.','.','.','.','.'], ['.','.','.','.','.']],
            [['.','.','.', '.', '.'], ['.','.','.','.','.'], ['.','.','.','.','.'], ['.','.','.','.','.'], ['.','.','.','.','.']],
            [['.','.','.', '.', '.'], ['.','.','.','.','.'], ['.','.','#','.','.'], ['.','.','.','.','.'], ['.','.','.','.','.']],
            [['.','.','.', '.', '.'], ['.','.','.','.','.'], ['.','.','.','.','.'], ['.','.','.','.','.'], ['.','.','.','.','.']],
            [['.','.','.', '.', '.'], ['.','.','.','.','.'], ['.','.','.','.','.'], ['.','.','.','.','.'], ['.','.','.','.','.']]]
@pytest.mark.parametrize("input_array, output_len, output_array", [
                         (array1, 3, array27),
                         (array27, 5, array125),
                         (array125, 7, None)
                         ])
def test_grow_by_one(input_array, output_len, output_array):

    output = grow_by_one(input_array)
    assert len(output) == len(output[0]) == len(output[0][0]) == output_len
    if output_array:
        for idx, z in enumerate(output):
            assert z == output_array[idx]


def grow_by_one(array_3d):
    assert len(array_3d) == len(array_3d[0]) == len(array_3d[0][0])
    new_array = []
    for z in array_3d:
        padded_layer = pad_2d_with_floor(z)
        new_array.append(pad_2d_with_floor(z))
    x_dim = len(new_array[0])
    y_dim = len(new_array[0][0])
    new_slice = [['.']*x_dim for x in range(y_dim)]
    new_array.append(new_slice)
    new_array.insert(0, new_slice)
    return new_array

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
    print(len(array_3d))

    grow_by_one(array_3d)

    return array_3d


def part_two(input_list):

    pass


if __name__ == "__main__":

    part_one(example1)
    part_two(input_list)
