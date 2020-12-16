#!/usr/bin/env python3
import pytest
import re

input_list = []
with open('day16.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(item)

rules = input_list[:input_list.index("your ticket:")]
nearby_tickets = input_list[input_list.index("nearby tickets:")+1:]

def part_one(rules, tickets):

    range_strings = []
    for rule in rules:
        parts = rule.split(" ")
        RANGE_RE = r"[0-9]+-[0-9]+"
        for part in parts:
            if re.match(RANGE_RE, part):
                range_strings.append(part)

    valid_nums = []
    for r in range_strings:
        low_bound = int(r.split("-")[0])
        hi_bound = int(r.split("-")[1]) + 1
        valid_nums += list(range(low_bound, hi_bound))

    valid_nums = sorted(set(valid_nums))

    invalid_sum = 0
    for ticket in tickets:
        for val in ticket.split(","):
            if int(val) not in valid_nums:
                invalid_sum += int(val)

    print("Part 1")
    print(invalid_sum)


def part_two(input_list):

    pass

if __name__ == "__main__":

    part_one(rules, nearby_tickets)
    part_two(input_list)
