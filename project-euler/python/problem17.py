import pytest



def count_1_9():
    return 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4

def count_10_19():
    # ten
    # eleven
    # twelve
    # thirteen
    # fourteen
    # fifteen
    # sixteen
    # seventeen
    # eighteen
    # nineteen
    return 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8


def count_20_99():
    # twenty, thirty, forty..
    prefixes = 6 + 6 + 5 + 5 + 5 + 7 + 6 + 6
    # for 8 decades
    return 10*prefixes + 8*count_1_9()

def count_century(prefix):
    # one hundred
    # one hundred and one
    # one hundred and two
    hundred = len("hundred")
    hundred_and = hundred + len("and")
    return len(prefix) + hundred + 99*(len(prefix) + hundred_and) + count_1_99()

def count_1_99():
    return count_1_9() + count_10_19() + count_20_99()

def count_1000():
    # one-thousand
    return 3 + 8

def count_100_999():
    sum =  count_century("one") + \
           count_century("two") + \
           count_century("three") + \
           count_century("four") + \
           count_century("five") + \
           count_century("six") + \
           count_century("seven") + \
           count_century("eight") + \
           count_century("nine")
    return sum

def count_1_1000():
    return count_1_99() + count_100_999() + count_1000()



print(count_1_1000())

def test_count_1_9():
    assert count_1_9() == 36

def test_count_10_19():
    assert count_10_19() == 70

def test_count_20_99():
    assert count_20_99() == 748

def test_count_1_99():
    assert count_1_99() == 854

def test_count_100_999():
    assert count_100_999() == 20259

