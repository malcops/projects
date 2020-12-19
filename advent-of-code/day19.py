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
                rhs = item.split(": ")[1]
                rules[lhs] = rhs
            else:
                messages.append(item)

print(rules)
print(messages)

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

    assert check_message(rules, msg) == validity


def check_message(rules, msg):

    rules_sub = dict(rules)

    FINISHED_RE = r"(^([ a-z|)(])+$)" 
    it = 0
    while not re.match(FINISHED_RE, rules_sub[0]):
    # while it < 5:
        for idx, char in enumerate(rules_sub[0]):
            if char.isnumeric():
                if '|' in rules[int(char)]:
                    str_to_add = "(" + rules[int(char)] + ")"
                else:
                    str_to_add = rules[int(char)]
                rules_sub[0] = rules_sub[0].replace(char, str_to_add)
                print(rules_sub[0])
        it += 1

    regex_string = rules_sub[0].replace(" ", "")
    print(regex_string)

    MESSAGE_RE = r"^{}$".format(regex_string)

    return bool(re.match(MESSAGE_RE, msg))

def part_one(rules_dict, msg_list):
    # number of messages that completely match rule 0

    check_message(rules_dict, msg_list[0])

    print("Part1: ", count)



def part_two():

    pass


if __name__ == "__main__":

    part_one(rules, messages)
    part_two()
