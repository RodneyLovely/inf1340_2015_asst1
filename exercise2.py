#!/usr/bin/env python


__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs:

    Expected Outputs:

    Errors:

    """

    print("Error")

def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name
    Inputs: an integer not less than 3, nor greater than 10
    Expected Outputs: The name of a shape, e.g.: triangle, square,... decagon
    Errors: an int less than 3, or an int greater than 10
    """
    sides = raw_input("Enter the number of sides your shape has?: ")

    if sides == "3":
        print("Triangle")
    elif sides == "4":
        print("Square")
    elif sides == "5":
        print("Pentagon")
    elif sides == "6":
        print("Hexagon")
    elif sides == "7":
        print("Heptagon")
    elif sides == "8":
        print("Octogon")
    elif sides == "9":
        print("Nonagon")
    elif sides == "10":
        print("Decagon")
    else:
        print("ERROR")

# elif sides <= "2" or sides > "10":
#   print("ERROR") will also work in place of "else"
# I think we can definitely make this look more elegant;
# just getting the basic concept down

name_that_shape()