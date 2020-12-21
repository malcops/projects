#!/usr/bin/env python3
import pytest
import re

messages = []
rules = dict()
with open('day19.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            if ':' in item:
                lhs = int(item.split(": ")[0])
                if '|' not in item:
                    rhs = item.split(": ")[1].replace("\"", "")
                else:
                    rhs = item.split(": ")[1].replace("\"", "")
                    # rhs = "(" + item.split(": ")[1].replace("\"", "") + ")"
                rules[lhs] = rhs
            else:
                messages.append(item)

print(rules)
# print(messages)

example0_rules = {0: "1 2", 1: "a",
                  2: "1 3 | 3 1", 3: "b"}

example1_rules = {0: "4 1 5", 1: "2 3 | 3 2",
                  2: "4 4 | 5 5", 3: "4 5 | 5 4",
                  4: "a", 5: "b"}

@pytest.mark.parametrize("rules, msg, validity", [
                        (example0_rules, "aab", True),
                        (example0_rules, "aba", True),
                        (example0_rules, "baa", False),

                        (example1_rules, "ababbb", True),
                        (example1_rules, "abbbab", True),
                        (example1_rules, "bababa", False),
                        (example1_rules, "aaabbb", False),
                        (example1_rules, "aaaabbb", False)
                         ])
def test_check_message(rules, msg, validity):

    regex = evaluate(rules, 0)
    MESSAGE_RE = r"^{}$".format(regex)   
    assert bool(re.match(MESSAGE_RE, msg)) == validity


def evaluate(rules, idx):
    '''returns regex string of rules dictionary'''
    if rules[idx] in ["a", "b"]:
        return rules[idx]
    parts = rules[idx].split(" | ")
    for j,p in enumerate(parts):
        parts[j] = '(' + ''.join(evaluate(rules, int(n)) for n in p.split()) + ')'
    return '(' + '|'.join(parts) + ')'


def part_one(rules_dict, msg_list):

    regex_string = evaluate(rules_dict, 0)
    print(regex_string)

    MESSAGE_RE = r"^{}$".format(regex_string)
    count = 0
    for msg in msg_list:
        if re.match(MESSAGE_RE, msg):
            count += 1

    print("Part1: ", count)



def part_two():

    pass


if __name__ == "__main__":

    part_one(rules, messages)
    part_two()
