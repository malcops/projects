import pytest

from problem3 import is_prime


def find_next_prime(x):
    """given a prime number, find the next prime"""
    x += 1
    while(not is_prime(x)):
        x += 1
    return x


def find_nth_prime(n):

    # idx 1 prime = 2
    idx = 1
    nth_prime = 2

    while not (idx == n):
        nth_prime = find_next_prime(nth_prime)
        idx += 1

    return nth_prime


def test_find_nth_prime():
    assert find_nth_prime(5) == 11
    assert find_nth_prime(6) == 13


def test_find_next_prime():

    assert find_next_prime(2) == 3
    assert find_next_prime(3) == 5
    assert find_next_prime(5) == 7
    assert find_next_prime(7) == 11
    assert find_next_prime(11) == 13

def answer():
    print(find_nth_prime(10001))

