# -*- coding: UTF-8 -*-

"""
Welcome to exercise 3 of set 2.

Modify each function until the tests pass.
"""


def is_odd(a_number):
    if a_number % 2 == 0 :
        return False
    else:
        return True
    """Return True if a_number is odd, and False if a_number is even.

    Look into modulo division using the '%' operator as one way of doing this.

    e.g. 4 % 2 = 0
        13 % 12 = 1
        3 % 2 = 1

    So if a_number modulo two is zero, then it's even.
    if a_number%2 == 0 :
        return True
    else:
        return False

"""
def fix_it(moves, should_move):
    """
    Using the engineering flowchart (in week2 folder of the CODE1161-2019
    repo engineeringFlowchart.png) for the rules, return the apropriate
    response to the input parameters.
    Use conditional statements: if, else, elif etc.
    This function should return either:
    "WD-40"
    "Duct Tape"
    "No Problem"

    Most people write this function with 4 return statements.
    As an extra challenge, see if you can get that down to three. return None
    """
    if moves==True:
        if should_move==False:
            return "Duct Tape"
        else:
            return "No Problem"
    elif moves==False:
        if should_move==True:
            return "WD-40"
        else:
            return "No Problem"

    #elif (moves == True + should_move == True) or (moves==False and should_move==False):
    #    return "No Problem"
    # ...



def loops_preview():
    cl = []
    for i in range(10):
        cl.append("💩")
    return cl

        # choc_list = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "act not the 9th"]
        # needed_list = ["💩"]
        # for i in range(choc_list):
        #   return i + needed_list
        # choc_list.append("💩")
        # return "the" + choc_list



def loops_1a():
    """Make 10 stars.
    
    Using a for loop
    return a list of 10 items, each one a string with exacly one star in it.
    E.g.: ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    """
    loops_1a = []
    for i in range(10):
        loops_1a.append('*')
    return loops_1a


def loops_1c(number_of_items=5, symbol="#"):
    loops_1c = []
    for i in range(number_of_items):
        loops_1c.append(symbol)
    return number_of_items
    """Respond to variables.

    Return a list of number_of_items items, each one a
    string with exacly one symbol in it.
    E.g.: ['#', '#', '#', '#', '#']

    Remember that you're being passed arguments here. Don't hard code the number
    or the symbol, let it be whatever it wants to be.
    """
    # number_of_items = []
    # int(number_of_items)
    loops_1c = []
    for i in range(number_of_items):
        loops_1c.append(symbol)
    return number_of_items



def loops_2_preview():
    """Make a big square 💩field.

    return a list of 4 items, each one a list of 4 items,
    each one of those, a string with exacly one star in it.
    E.g.: [
            ['💩', '💩', '💩', '💩'],
            ['💩', '💩', '💩', '💩'],
            ['💩', '💩', '💩', '💩'],
            ['💩', '💩', '💩', '💩'],
        ]
    """
    field = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append("💩")
        field.append(row)
    return field


def loops_2():
    """Make a big square starfield.

    return a list of 10 items, each one a list of 10 items,
    each one of those, a string with exacly one star in it.
    E.g.: [
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ]
    """
    star_1 =[]
    for i in range(10):
        star_2 = []
        for j in range(10):
            star_2.append('*')
        star_1.append(star_2)
    return star_1


def loops_3():
    l1 = []
    for i in range(10):
        l2 = []
        for j in range(10):
            l2.append(str(i))
        l1.append(l2)
    print(l1)   
    return l1
    """Make a rising block of numbers.

    Return this:
    [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2'],
        ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3'],
        ['4', '4', '4', '4', '4', '4', '4', '4', '4', '4'],
        ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5'],
        ['6', '6', '6', '6', '6', '6', '6', '6', '6', '6'],
        ['7', '7', '7', '7', '7', '7', '7', '7', '7', '7'],
        ['8', '8', '8', '8', '8', '8', '8', '8', '8', '8'],
        ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9']
    ]
    remember that range(10) produces a list of numbers from 0...9
    So for every step produced by `for i in range(10):` i is a different number
    TIP: notice that this needs to to return strings of numbers,
            so call str(number) to cast.
    """
    l1 = []
    for i in range(10):
        l2 = []
        for j in range(10):
            l2.append(str(j))
        l1.append(l2)
    print(l1)   
    return l1
            




def loops_4():
    l11 = []
    for i in range(10):
        l22 = []
        for j in range(10):
            l22.append(str(j))
        l11.append(l22)
    print(l11)   
    return l11
    """Make a block of numbers that rises left to right.


    Return this:
    [
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ]
    """
    l11 = []
    for i in range(10):
        l22 = []
        for j in range(10):
            l22.append(j)
        l11.append(str(l22))
    print(l11)   
    return l11
    # another way is
    # l11 = [] -- make a list
    # for i in range(10): -- 10 t.
    #     l11.append(range(10)) -- add to the list items in range from 0 to 9
        
        # l1 = []
        # for i in range(10):
        #l2 = []
        #for j in range(10):
        #   l2.append(range(10))
            
        #l1.append(l2)


def loops_5():
    l111 = []
    for i in range(10):
        l222 = []
        for j in range(5):
        #    l222.append("(i" + str(i) + "," + " " + "j" + str(j) + ")")
            l222.append("(i{}, j{})".format(i, j))
        l111.append(l222)
    print(l111)
    return l111
    """Make the coordinates of the block.

    Return this:
    [
        ["(i0, j0)", "(i0, j1)", "(i0, j2)", "(i0, j3)", "(i0, j4)"],
        ["(i1, j0)", "(i1, j1)", "(i1, j2)", "(i1, j3)", "(i1, j4)"],
        ["(i2, j0)", "(i2, j1)", "(i2, j2)", "(i2, j3)", "(i2, j4)"],
        ["(i3, j0)", "(i3, j1)", "(i3, j2)", "(i3, j3)", "(i3, j4)"],
        ["(i4, j0)", "(i4, j1)", "(i4, j2)", "(i4, j3)", "(i4, j4)"],
        ["(i5, j0)", "(i5, j1)", "(i5, j2)", "(i5, j3)", "(i5, j4)"],
        ["(i6, j0)", "(i6, j1)", "(i6, j2)", "(i6, j3)", "(i6, j4)"],
        ["(i7, j0)", "(i7, j1)", "(i7, j2)", "(i7, j3)", "(i7, j4)"],
        ["(i8, j0)", "(i8, j1)", "(i8, j2)", "(i8, j3)", "(i8, j4)"],
        ["(i9, j0)", "(i9, j1)", "(i9, j2)", "(i9, j3)", "(i9, j4)"]
    ]

    TIP:
    If you've got num_bottles, e.g. num_bottles = 8
    You can construct strings either by concatinating them:
        "There are " + str(num_bottles) + " green bottles"
    or by using format:
        "There are {} green bottles".format(num_bottles)
    or, my favourite, f-strings:
        f"There are {num_bottles} green bottles"
    you'll come to see the pros and cons of each over time.
    """
    l111 = []
    for i in range(10):
        l222 = []
        for j in range(5):
        #    l222.append("(i" + str(i) + "," + " " + "j" + str(j) + ")")
            l222.append("(i{}, j{})".format(i, j))
        l111.append(l222)
    print(l111)
    # are there 2 or 3 lists?
    # 1 big list + 10 lists inside + tuples???


def loops_6():
    l6 = []
    for i in range(10):
        l7=[]
        for j in range(i + 1):
            l7.append(str(j))
        l6.append(l7)
    return l6
    """Make a wedge of numbers.

    Return this:
    [
        ['0'],
        ['0', '1'],
        ['0', '1', '2'],
        ['0', '1', '2', '3'],
        ['0', '1', '2', '3', '4'],
        ['0', '1', '2', '3', '4', '5'],
        ['0', '1', '2', '3', '4', '5', '6'],
        ['0', '1', '2', '3', '4', '5', '6', '7'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ]
    You don't have to use a literal number in the range function.
    You can use a variable.
    TIP: look out for the starting condition.
    """
    l6 = []
    for i in range(10):
        l7=[]
        for j in range(i + 1):
            l7.append(j)
        l6.append(l7)
    return l6


def loops_7():
    l8 = []
    starr = ['*']
    spacee = [' ']
    for i in range(5):
        #    if spacee < i:
        row = spacee*(4 - i) + starr*(2*i + 1) + spacee*(4 - i)
        l8.append(row)
    return l8
    """Make a pyramid.

    Return this:
    [
        [' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' '],
        [' ', ' ', '*', '*', '*', '*', '*', ' ', ' '],
        [' ', '*', '*', '*', '*', '*', '*', '*', ' '],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*']
    ]
    or in more simple terms:
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
    (this is what will print when you test from inside this file)
    This is a hard problem. Use lots of experimentation and draw
    lots of diagrams!
    """
    l8 = []
    for i in range(5):
        l9 = []
        starr = '*'
        spacee = ' '
        for j in range(9):
            l9.append(spacee*(5 - i) + starr*(9 - j) + spacee*(5 - i))
        l8.append(l9)
    return l8
            # print(spacee*(9 - j) + starr + spacee* ) or something like that?
            # should i use indexation within a list?
            # print(spacee*4 + starr + spacee*4)
            # print(spacee*3 + starr*3 + spacee*3)
            # print(spacee*2 + starr*5 + spacee*2)
            # print(spacee*1 + starr*7 + spacee*1)
            # print(spacee*0 + starr*9 + spacee*0)
            # l9.append(spacee*(i - 1) + starr + spacee*(i - 1))
            # l9.append(spacee*(i - 2) + starr*3 + spacee*(i - 2))
            # l9.append(spacee*(i - 3) + starr*5 + spacee*(i - 3))
            # l9.append(spacee*(i - 4) + starr*7 + spacee*(i - 4))
            # l9.append(spacee*(i - 5) + starr*9 + spacee*(i - 5))


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    try:
        from helper import little_printer, minitest
        minitest(is_odd, [1], True)
        minitest(is_odd, [4], False)
        minitest(fix_it, [True, True], "No Problem")
        minitest(fix_it, [True, False], "WD-40")
        minitest(fix_it, [False, True], "Duct Tape")
        minitest(fix_it, [False, False], "No Problem")
        little_printer(loops_preview(), "loops_preview")
        little_printer(loops_1a(), "loops_1a")
        little_printer(loops_1c(4, "×°×"), "loops_1c")
        little_printer(loops_2_preview(), "loops_2_preview")
        little_printer(loops_2(), "loops_2")
        little_printer(loops_3(), "loops_3")
        little_printer(loops_4(), "loops_4")
        little_printer(loops_5(), "loops_5")
        little_printer(loops_6(), "loops_6")
        little_printer(loops_7(), "loops_7")
    except ModuleNotFoundError as e:
        print("⚠"*20, "\nWe're looking for a module that's missing. That's probably a problem that a tutor needs to figure out.\n")
        print(e)
        print("⚠"*20)
