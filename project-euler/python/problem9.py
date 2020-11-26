from math import sqrt


def pythagorean_sum(a, b, c):

    return a + b + c


def pythagorean_product(a, b, c):

    return a * b * c


def is_perfect_square(x):
    return ((x > -1) and (sqrt(x) % 1 == 0))


def answer():
    ret = 0
    for a in range(1, 1000, 1):
        for b in range(1, 1000, 1):
            c_sq = a**2 + b**2
            if (is_perfect_square(c_sq)):
                if (a + b + int(sqrt(c_sq)) == 1000):
                    print("a: {}\nb: {}\nc: {}\n".format(a, b, int(sqrt(c_sq))))
                    print("product is: {}\n".format(pythagorean_product(a, b, int(sqrt(c_sq)))))
                    return

answer()



def test_is_perfect_square():
    assert is_perfect_square(25) == True
    assert is_perfect_square(25.001) == False


def test_pythagorean_sum():
    assert pythagorean_sum(3, 4, 5) == 12


def test_pythagorean_product():
    assert pythagorean_product(3, 4, 5) == 60

