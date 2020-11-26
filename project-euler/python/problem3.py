from math import sqrt
import pytest

def is_prime(x):
    if x >=2:
        for y in range(2,x):
            if not (x % y):
                return False
    else:
        return False

    return True

def get_factors(x):
    """Find factors"""

    root = sqrt(x)
    start = int(root)

    # for odd number, only check for odd factors
    if not (x % 2):
        step = -1
    else:
        step = -2
        # Round start to odd number
        start = start // 2 * 2 + 1

    if root.is_integer():
        yield int(root)
        start += step

    for i in range(start, 0, step):
        if x % i == 0:
            yield i
            yield x // i

    return


def get_prime_factors(x):

    factors = sorted(list(get_factors(x)))
    prime_list = [y for y in factors if is_prime(y)]
    return prime_list


def test_get_prime_factors():
    assert get_prime_factors(13195) == [5, 7, 13, 29]


def test_get_factors():
    assert sorted(list(get_factors(33))) == [1, 3, 11, 33]
    assert sorted(list(get_factors(10))) == [1, 2, 5, 10]


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(29) == True

    assert is_prime(1) == False
    assert is_prime(10) == False
    assert is_prime(100) == False
    assert is_prime(124) == False

def answer():
    print(get_prime_factors(600851475143))

