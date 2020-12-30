#!/usr/bin/env python3
import pytest
import time

round1_p1 = [9,2,6,3,1]
round1_p2 = [5,8,4,7,10]

round2_p1 = [2,6,3,1,9,5]
round2_p2 = [8,4,7,10]

round3_p1 = [6,3,1,9,5]
round3_p2 = [4,7,10,8,2]

round4_p1 = [3,1,9,5,6,4]
round4_p2 = [7,10,8,2]

round5_p1 = [1,9,5,6,4]
round5_p2 = [10,8,2,7,3]

# recursive combat
round6_p1 = [9,5,6,4]
round6_p2 = [8,2,7,3,10,1]

round7_p1 = [5,6,4,9,8]
round7_p2 = [2,7,3,10,1]

round8_p1 = [6,4,9,8,5,2]
round8_p2 = [7,3,10,1]

round9_p1 = [4,9,8,5,2]
round9_p2 = [3,10,1,7,6]


input_list = []
with open('day22.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(item)

p2_start = input_list.index("Player 2:")
deck1 = [int(x) for x in input_list[1:p2_start]]
deck2 = [int(x) for x in input_list[p2_start+1:]]


@pytest.mark.parametrize("deck1, deck2, deck1_after, deck2_after", [
                        (round1_p1, round1_p2, round2_p1, round2_p2),
                        (round2_p1, round2_p2, round3_p1, round3_p2),
                        (round3_p1, round3_p2, round4_p1, round4_p2),
                        (round4_p1, round4_p2, round5_p1, round5_p2),
                        (round5_p1, round5_p2, round6_p1, round6_p2),
                        (round6_p1, round6_p2, round7_p1, round7_p2),
                         ])
def test_play_round(deck1, deck2, deck1_after, deck2_after):

    d1, d2 = play_round(deck1, deck2)
    assert d1 == deck1_after
    assert d2 == deck2_after


def play_round(deck1, deck2):


    if deck1[0] > deck2[0]:
        deck1.append(deck1.pop(0))
        deck1.append(deck2.pop(0))
    else:
        deck2.append(deck2.pop(0))
        deck2.append(deck1.pop(0))

    return deck1, deck2


@pytest.mark.parametrize("deck1, deck2, deck1_after, deck2_after", [
                        (round1_p1, round1_p2, round2_p1, round2_p2),
                        (round2_p1, round2_p2, round3_p1, round3_p2),
                        (round3_p1, round3_p2, round4_p1, round4_p2),
                        (round4_p1, round4_p2, round5_p1, round5_p2),
                        (round5_p1, round5_p2, round6_p1, round6_p2),
                        (round6_p1, round6_p2, round7_p1, round7_p2),
                        (round7_p1, round7_p2, round8_p1, round8_p2),
                        (round8_p1, round8_p2, round9_p1, round9_p2),
                        (round9_p1, round9_p2, None, None),
                         ])
def test_play_recursive_combat(deck1, deck2, deck1_after, deck2_after):
    d1, d2 = play_recursive_combat(deck1, deck2)
    assert d1 == deck1_after
    assert d2 == deck2_after


def play_recursive_combat(deck1, deck2):

    print(deck1, deck2)

    winner = 0
    prev_hands = []
    hand = hash(str(deck1 + deck2))
    # TODO
    if hand in prev_hands:
        print("Deck1 wins")
        return deck1, deck2, 1
    else:
        prev_hands.append(hand)

    while deck1 and deck2:
        if deck1[0] < len(deck1) and deck2[0] < len(deck2):
            print("Recursive combat")
            d1, d2 = play_recursive_combat(deck1[1:1+deck1[0]], deck2[1:1+deck2[0]])
        else:
            d1, d2 = play_round(deck1, deck2)

    if deck1:
        print("Deck1 wins")
        print(calculate_score(deck1))
    else:
        print("Deck2 wins")
        print(calculate_score(deck2))

    return deck1, deck2   

def calculate_score(deck):

    sum = 0
    for it, x in enumerate(list(reversed(deck))):
        sum += (it+1) * x

    return sum


def part_one(deck1, deck2):

    play_game(deck1, deck2)


def play_game(deck1, deck2):

    while deck1 and deck2:
        deck1, deck2 = play_round(deck1, deck2)

    if deck1:
        print("Deck1 wins")
        print(calculate_score(deck1))
    else:
        print("Deck2 wins")
        print(calculate_score(deck2))

    return deck1, deck2


def part_two(deck1, deck2):
    
    play_recursive_combat(deck1, deck2)


if __name__ == "__main__":

    start = time.time()
    part_one(deck1, deck2)
    stop = time.time()
    print("time: ", stop - start)

    start = time.time()
    part_two(deck1, deck2)
    stop = time.time()
    print("time: ", stop - start)
