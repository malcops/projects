import pytest
from problem3 import get_factors


def get_proper_divisors(x):
    factors = sorted(list(get_factors(x)))
    # remove last factor in list (which is equal to x)
    factors.pop()
    return factors

sums = [0] * 10000
for i in range(0,10000):
    sums[i] = sum(get_proper_divisors(i))

assert sums[220] == 284
assert sums[284] == 220

pairs = []
for idx, total in enumerate(sums):
    # 1. < 10000 to avoid out-of-bounds access
    # 2. check that sums at the index of current sum equals the current index
    # 3. check that they are not equal
    if total < 10000 and sums[total] == idx and sums[idx] != idx:
        pairs.append(idx)
        print("pair: {}  {}".format(idx, sums[total]))

print(pairs)
print(sum(pairs))

def test_get_proper_divisors():
    assert get_proper_divisors(220) == [1,2,4,5,10,11,20,22,44,55,110]
    assert get_proper_divisors(284) == [1,2,4,71,142]
    assert sum(get_proper_divisors(220)) == 284
    assert sum(get_proper_divisors(284)) == 220

