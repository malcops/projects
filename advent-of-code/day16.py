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
    valid_tickets = []
    for ticket in tickets:
        valid_ticket = True
        for val in ticket.split(","):
            if int(val) not in valid_nums:
                invalid_sum += int(val)
                valid_ticket = False
        if valid_ticket:
            valid_tickets.append(ticket)

    print("Part 1")
    print(invalid_sum)
    print(len(tickets))
    print(len(valid_tickets))
    return valid_tickets



@pytest.mark.parametrize("rules, tickets", [
                        (["class: 0-1 or 4-19",
                          "row: 0-5 or 8-19",
                          "seat: 0-13 or 16-19"], ["3,9,18", "15,1,5", "5,14,9"]),
                         ])
def test_part_two(rules, tickets):

    mapping = part_two(rules, tickets)
    assert mapping['row'] == 0
    assert mapping['class'] == 1
    assert mapping['seat'] == 2


def part_two(rules, valid_tickets):

    rules_dict = dict()
    for rule in rules:
        field = rule.split(":")[0]
        valid_nums = []
        parts = rule.split(" ")
        RANGE_RE = r"[0-9]+-[0-9]+"
        for part in parts:
            if re.match(RANGE_RE, part):
                low_bound = int(part.split("-")[0])
                hi_bound  = int(part.split("-")[1]) + 1
                valid_nums += list(range(low_bound, hi_bound))
            rules_dict[field] = sorted(set(valid_nums))


    tickets = []
    for t in valid_tickets:
        tickets.append(t.split(","))

    mapping = {f: [] for f in rules_dict}
    indexes = []
    for idx, x in enumerate(tickets):
        indexes.append([int(r[idx]) for r in tickets])

    print(rules_dict)
    print(tickets)
    print(indexes)

    assigned = []
    for field in rules_dict:
        valid = []
        for idx, nums in enumerate(indexes):
            all_there = all(item in rules_dict[field] for item in nums)
            if all_there:
                print(idx, nums)
                print(rules_dict[field])
                valid.append(idx)
                print(valid)

        mapping[field] = valid
        if len(valid) == 1:
            assigned.append(valid[0])

    print(mapping)
    print(assigned)

    return mapping



if __name__ == "__main__":

    valid_tickets = part_one(rules, nearby_tickets)
    part_two(rules, valid_tickets)
