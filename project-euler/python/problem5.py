import pytest

def is_evenly_divisible(num, denom):

    ret = not (num % denom)

    return ret


def attempt(num, max_div):

    ret = True
    for i in range(max_div, 0, -1):
        if not is_evenly_divisible(num, i):
            ret = False
            return ret
    return ret


def test_attempt():
    assert attempt(2520, 10) == True
    assert attempt(12, 4) == True
    assert attempt(12, 5) == False

def test_is_evenly_divisible():

    assert is_evenly_divisible(20, 1) == True
    assert is_evenly_divisible(20, 3) == False
    assert is_evenly_divisible(100, 3) == False
    assert is_evenly_divisible(100, 10) == True
    assert is_evenly_divisible(49, 7) == True
    assert is_evenly_divisible(49, 8) == False

if __name__ == "__main__":

    finished = False
    num = 20
    max_div = 20
    while(not finished):
        if attempt(num, max_div):
            print(num)
            finished = True
        else:
            num += 20

    print("Complete!")

