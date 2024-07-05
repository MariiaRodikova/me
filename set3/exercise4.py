# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""

import math
import random


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll 1) give it a range to guess inside, and then 2) use binary search to home
    in on the actual_number.

    Each guess, 1) print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}

    This will be quite hard, especially hard if you don't have a good diagram!

    Use the VS Code debugging tools a lot here. It'll make understanding
    things much easier.
    """
    tries = 0
    guess = 0

    print("numbers (again)")
    low = input("Lower bound: ")
    low = int(low)
    print(f"A number between {low} and _ ?")
    high = input("Enter an upper bound: ")
    high = int(high)
    print(f"OK then, a number between 0 and {high} ?")
    for j in range(low, high):
        l = []
        l.append(j)
    
    #actual_number = l.randint(low, high)
    actual_number = input("Searching for ")
    actual_number = int(actual_number)
    while actual_number > low and actual_number < high:
        two = 2
        middle = len(l)//two
        print(f"low:{low}, mid:{middle}, high:{high}")
        if actual_number == middle:
            return tries
        elif actual_number > middle:
            low = middle
            middle = (high - low)/2 
            tries = tries + 1
            return binary_search(low, high, actual_number)
        elif actual_number < middle:
            high = middle
            middle = (high - low)/2
            tries = tries + 1
            return binary_search(low, high, actual_number)
    binary_search(low, high, actual_number)

#QUESTIONs:
#1) why it goes back when runs after the high input


    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
