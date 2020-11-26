import pytest

def sum_of_squares(x):

    sum = 0
    for i in range(1,x+1):
        sum += i**2
    return sum


def square_of_sum(x):

    return sum(range(1, x+1))**2


def test_sum_square_difference():

    assert (square_of_sum(10) - sum_of_squares(10)) == 2640


def test_sum_of_squares():

    assert sum_of_squares(10) == 385


def test_square_of_sum():

    assert square_of_sum(10) == 3025

def answer():

    print(square_of_sum(100) - sum_of_squares(100))

