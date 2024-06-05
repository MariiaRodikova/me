"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ["what", "does", "this", "line", "do", "?"]
# I think this will return every item from the list 
for word in some_words:
    print(word)
# Actually return items from the list
# Does the same as the upper one because x is similar to words and python does not mind how you call an item
for x in some_words:
    print(x)
# Does actually the same and return items from the list
# Prints the list 
print(some_words)
# Really have returned the list 
# If the quantity of items in the list is bigger than 3, will tell that the list contains more than 3 words. If false, will return nothing.
if len(some_words) > 3:
    print("some_words contains more than 3 words")
    # Does as expected.


def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # Return a list contains something
    print(platform.uname())


usefulFunction()
