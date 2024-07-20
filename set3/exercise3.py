"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.#
"""

import random


def advancedGuessingGame():
    print("You are going to guess a number between from_")
    lower_bound = input()
    # check whether lb is an integer or not with while loop?
    #if lower_bound.isdigit():
    #    print("OK it's settled")
    #else:
    #    print("Number, sir/madam!")
    #    lower_bound = input()
    while type(lower_bound) != int:
        try:
            lower_bound = int(lower_bound)
            print("OK it's settled")
        except ValueError:
            print("Number, sir/madam!")
            lower_bound = input()
    print(f"A number between {lower_bound} and _ ?")
    higher_bound = input("Enter an upper bound: ")
    while type(higher_bound) != int:
        try:
            higher_bound = int(higher_bound)
            print("OK it's settled")
        except ValueError:
            print("Number, sir/madam!")
            higher_bound = input()
    print(f"OK then, a number between 0 and {higher_bound} ?")
    #higher_bound = int(higher_bound)
    #int(lower_bound)
    actualNumber = random.randint(lower_bound, higher_bound)
    guessed = False
    while not guessed:
        users_guess = int(input("Now, your guess: "))
        print(f'Ok, so far you think it was {users_guess}')
        if users_guess == actualNumber:
            print("Why are you so lucky?")
            guessed = True
        elif users_guess < actualNumber:
            print("Well, it's a bit bigger.")
            users_guess = int(input("Now, your new guess: "))
        elif users_guess > actualNumber:
            print("Well, it's smaller. Try again.")
        elif guessed not in range(lower_bound, higher_bound):
        #  elif (guessed < lower_bound) | (guessed > higher_bound):
            print("Have you already forgotten what we are playing here?..")
    return "You got it!"



    #"Play a guessing game with a user.

    #The exercise here is to rewrite the exampleGuessingGame() function
    #from exercise 3, but to allow for:
    #* a lower bound to be entered, e.g. guess numbers between 10 and 20
    #* ask for a better input if the user gives a non integer value anywhere.
    # I.e. throw away inputs like "ten" or "8!" but instead of crashing
    #ask for another value.
    #chastise them if they pick a number outside the bounds.
    #see if you can find the other failure modes.
    #There are three that I can think of. (They are tested for.)

    #NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    #be able to eventually, it'd be better to take the code from exercise 2 and
    #merge it with code from excercise 1.
    #You can refactor a bit, you should refactor a bit! Don't put the code all
    #inside this function, think about reusable chunks of code that you can call
    #in several places.
    #Remember to think modular. Try to keep your functions small and single
    #purpose if you can!
    
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
