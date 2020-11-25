import pytest
from problem3 import get_factors


def number_of_factors(x):
    return len(sorted(list(get_factors(x))))


def test_number_of_factors():

    assert number_of_factors(15) == 4
    assert number_of_factors(21) == 4
    assert number_of_factors(28) == 6

sum = 0
for i in range(1,100000):
    sum += i
    if number_of_factors(sum) > 500:
        print("answer: {}".format(sum))
        break

