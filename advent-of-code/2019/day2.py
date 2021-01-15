#!/usr/bin/env python3
import pytest
import time


def run_intcode(instructions, pos=0):

    opcode = instructions[pos]
    if opcode == 99:
        pass
    elif opcode == 1:
        x1 = instructions[pos+1]
        x2 = instructions[pos+2]
        pos = instructions[pos+3]
        instructions[pos] = instructions[x1] + instructions[x2]
    elif opcode == 2:
        x1 = instructions[pos+1]
        x2 = instructions[pos+2]
        pos = instructions[pos+3]
        instructions[pos] = instructions[x1] * instructions[x2]
    else:
        assert 1 == 0

    return opcode, instructions


def run_program(input_list):

    instructions = input_list[:]
    pos = 0
    opcode = 0
    while opcode != 99:
        opcode, instructions = run_intcode(instructions, pos)
        pos += 4

    # print("final instructions: ", instructions)
    return instructions


@pytest.mark.parametrize("instructions, final_instructions", [
                         ([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]),
                         ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
                         ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
                         ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
                         ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99])
                         ])
def test_run_program(instructions, final_instructions):

    assert final_instructions == run_program(instructions)


def part_one(input_list):

    instructions = input_list[:]
    instructions[1] = 12
    instructions[2] = 2

    final = run_program(instructions)
    print("Part 1: ", final[0])


def part_two(input_list):

    instructions = input_list[:]
    for noun in range(100):
        for verb in range(100):
            loop_instructions = instructions[:]
            loop_instructions[1] = noun
            loop_instructions[2] = verb
            final = run_program(loop_instructions)
            if final[0] == 19690720:
                print("Part 2: ", 100 * noun + verb)
                break


if __name__ == "__main__":

    example = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    puzzle_input = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 19, 6, 23, 2, 13, 23, 27, 1, 27, 13, 31, 1, 9, 31, 35, 1, 35, 9, 39, 1, 39, 5, 43, 2, 6, 43, 47, 1, 47, 6, 51,
                    2, 51, 9, 55, 2, 55, 13, 59, 1, 59, 6, 63, 1, 10, 63, 67, 2, 67, 9, 71, 2, 6, 71, 75, 1, 75, 5, 79, 2, 79, 10, 83, 1, 5, 83, 87, 2, 9, 87, 91, 1, 5, 91, 95,
                    2, 13, 95, 99, 1, 99, 10, 103, 1, 103, 2, 107, 1, 107, 6, 0, 99, 2, 14, 0, 0]

    start = time.time()
    part_one(puzzle_input)
    stop = time.time()
    print("time: ", stop - start)

    start = time.time()
    part_two(puzzle_input)
    stop = time.time()
    print("time: ", stop - start)
