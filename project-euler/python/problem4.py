import pytest


def is_palindrome(x):

    string = str(x)
    length = len(string)
    first = string[:int(length/2)]
    second = string[length:int(length/2) - 1:-1]
    return first == second


max = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        x = i*j
        if x > max:
            if is_palindrome(x):
                max = x

print(max)



def test_is_palindrome():
    assert True == is_palindrome(1001)
    assert True == is_palindrome(200002)
    assert True == is_palindrome(123321)

