import pytest

value_dict = {"A":1, "B":2, "C":3, "D":4, "E":5,
              "F":6, "G":7, "H":8, "I":9, "J":10,
              "K":11, "L":12, "M":13, "N":14, "O":15,
              "P":16, "Q":17, "R":18, "S":19, "T":20,
              "U":21, "V":22, "W":23, "X":24, "Y":25,
              "Z": 26}


def name_value(name):
    value = 0
    for letter in name:
        value += value_dict.get(letter)
    return value





with open("problem22_names.txt", "r+") as f:
    names = sorted(f.read().replace('"','').replace("\n", "").split(','),key=str)
    sum = 0

    for idx, name in enumerate(names):
        sum += name_value(name) * (idx+1)

    print(sum)



def test_name_value():
    assert name_value("COLIN") == 53
    assert name_value("ALONSO") == 76

