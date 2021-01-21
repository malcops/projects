#!/usr/bin/env python3
import pytest
import time

input_list = []
with open('day3.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(list(item.split(',')))

wire1 = input_list[0]
wire2 = input_list[1]

example_wire1 = ["R8", "U5", "L5", "D3"]
example_wire2 = ["U7", "R6", "D4", "L4"]

example2_wire1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
example2_wire2 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]

example3_wire1 = ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"]
example3_wire2 = ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]


@pytest.mark.parametrize("wire1, wire2, final_answer", [
                         (example_wire1, example_wire2, 6),
                         (example2_wire1, example2_wire2, 159),
                         (example3_wire1, example3_wire2, 135),
                         ])
def test_part_one(wire1, wire2, final_answer):

    assert final_answer == part_one(wire1, wire2)


def part_one(wire1_list, wire2_list):

    wire1_instructions = parse_instructions(wire1_list)
    wire1_locations = traverse_wire(wire1_instructions)

    wire2_instructions = parse_instructions(wire2_list)
    wire2_locations = traverse_wire(wire2_instructions)

    ans = find_closest_intersection(wire1_locations, wire2_locations)

    print("Part1: ", ans)
    return ans


def part_two(input_list):

    pass


def traverse_wire(instructions):

    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    locations = []
    x = 0
    y = 0
    for ins in instructions:
        vector = directions[ins[0]]
        magnitude = ins[1]
        for loc in range(magnitude):
            x += vector[0]
            y += vector[1]
            locations.append((x, y))

    return locations


def find_closest_intersection(wire1, wire2):

    crossings = list(set(wire1).intersection(wire2))
    print(crossings)
    closest_distance = 1000000
    for crossing in crossings:
        distance = abs(crossing[0]) + abs(crossing[1])
        if distance < closest_distance:
            closest_distance = distance

    return closest_distance


def parse_instructions(instruction_list):

    instructions = []
    for ins in instruction_list:
        dir = ins[0]
        num = int(ins[1:])
        instructions.append((dir, num))
    print(instructions)
    return instructions


if __name__ == "__main__":

    start = time.time()
    part_one(wire1, wire2)
    stop = time.time()
    print("time: ", stop - start)

    start = time.time()
    part_two(input_list)
    stop = time.time()
    print("time: ", stop - start)
