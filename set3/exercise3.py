"""Set 3, Exercise 3.

Steps on the way to making your own guessing game
"""

import random

def advancedGuessingGame():
    """Play a guessing game with a user.
        The exercise here is to rewrite the exampleGuessingGame() function
        from exercise 3, but to allow for:
        * a lower bound to be entered, e.g. guess numbers between 10 and 20
        * ask for a better input if the user gives a non integer value anywhere.
        I.e. throw away inputs like "ten" or "8!" but instead of crashing
        ask for another value.
        chastise them if they pick a number outside the bounds.
        see if you can find the other failure modes.
        There are three that I can think of. (They are tested for.)
        NOTE: whilst you CAN write this from scratch, and it'd be good for you to
        be able to eventually, it'd be better to take the code from exercise 2 and
        merge it with code from excercise 1.
        You can refactor a bit, you should refactor a bit! Don't put the code all
        inside this function, think about reusable chunks of code that you can call
        in several places.
    #Remember to think modular. Try to keep your functions small and single
    #purpose if you can!
    # the tests are looking for the exact string "You got it!". Don't modify that!
    """
    print("You are going to guess a number from_")
    lower_bound = input()
    while type(lower_bound) != int:
        try:
            lower_bound = int(lower_bound)
            print("OK it's settled")
        except ValueError:
            print(f"Number, sir/madam,not {lower_bound}!")
            lower_bound = input()
    print(f"A number between {lower_bound} and _ ?")
    higher_bound = input("Enter an upper bound: ")
    while type(higher_bound) != int:
        try:
            higher_bound = int(higher_bound)
            print("OK it's settled")
        except ValueError:
            print(f"Number, sir/madam, not {higher_bound}!")
            higher_bound = input()
    if lower_bound > higher_bound:
        print("Now upper bound is smaller than the lower bound, try again ")
        higher_bound = input("Enter an upper bound: ")
    elif higher_bound == lower_bound:
        print ("They are equal. Try again ")
        higher_bound = input("Enter an upper bound: ")
    elif higher_bound - lower_bound == 1:
        print ("And what we are going to guess? Try again ")
        higher_bound = input("Enter an upper bound: ")
    print(f"OK then, a number between {lower_bound} and {higher_bound} ?")
    actualNumber = random.randint(lower_bound, higher_bound)
    guessed = False
    while not guessed:
        users_guess = int(input("Now, your guess: "))
        if users_guess == actualNumber:
            print("Why are you so lucky?")
            guessed = True
        #elif users_guess not in range(lower_bound - 1, higher_bound+1):
        elif (users_guess < lower_bound) | (users_guess > higher_bound):
            print("Have you already forgotten what we are playing here?..")
        elif users_guess < actualNumber:
            print(f"Well, it's a bit bigger than {users_guess}. Try again ")
        elif users_guess > actualNumber:
            print(f"Too small, {users_guess} is smaller than the actual number. try again :'( ")
    return "You got it!"





if __name__ == "__main__":
    print(advancedGuessingGame())
