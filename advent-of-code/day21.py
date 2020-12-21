#!/usr/bin/env python3
import numpy as np
import pytest
import time

foods = []
with open('day21.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            foods.append(item)

# print(foods)

example = [
"mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
"trh fvjkl sbzzf mxmxvkd (contains dairy)",
"sqjhc fvjkl (contains soy)",
"sqjhc mxmxvkd sbzzf (contains fish)",
]



def part_one(input_list):
    
    ingredients = []
    allergens = []
    my_dict = dict()
    for line in input_list:
        ing = list(filter(None, line.split("(")[0].split(" ")))
        allerg = list(filter(None, line.split("contains")[1].replace(")", "").replace(",","").split(" ")))
        for a in allerg:
            if a not in my_dict:
                my_dict[a] = list(ing)
            else:
                print(list(set(my_dict[a]).intersection(ing)))
                my_dict[a] = list(set(my_dict[a]).intersection(ing))
        ingredients += ing
        allergens += allerg
    ingredients = list(set(ingredients))
    allergens = list(set(allergens))

    # list is of ingredients that MIGHT have this allergen
    print(my_dict)

    safe_ingredients = ingredients[:]
    for d in my_dict:
        for i in my_dict[d]:
            if i in safe_ingredients:
                safe_ingredients.remove(i)
    
    print(safe_ingredients)

    counts = dict()
    for i in safe_ingredients:
        counts[i] = 0
    for line in input_list:
        ing = list(filter(None, line.split("(")[0].split(" ")))
        for i in ing:
            if i in safe_ingredients:
                counts[i] = counts[i] + 1
    print(counts)
    print("Part1 :", sum(counts.values()) )

def part_two(input_list):
    pass


if __name__ == "__main__":

    start = time.time()
    part_one(example)
    stop = time.time()
    print("time: ", stop - start)

    start = time.time()
    part_two(foods)
    stop = time.time()
    print("time: ", stop - start)