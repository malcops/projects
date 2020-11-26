import pytest

def seqEven(n):
    return n/2


def seqOdd(n):
    return 3*n + 1


def calc_chain(x):
    chain = 1
    while (x != 1):
        if (x % 2):
            x = seqOdd(x)
        else:
            x = seqEven(x)
        chain += 1
    return chain


max_chain = 0
for x in range(1,1000000):
    y = calc_chain(x)
    if y > max_chain:
        max_chain = y
        print("start: {}\nmax_chain: {}".format(x, max_chain))


def test_calc_chain():
    assert calc_chain(13) == 10
    assert calc_chain(40) == 9
    assert calc_chain(20) == 8
    assert calc_chain(1)  == 1

