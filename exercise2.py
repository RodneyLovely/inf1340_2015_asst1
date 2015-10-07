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
    Expected Outputs: The name of a shape, e.g.: triangle, quadrilateral,... decagon
    Errors: an int less than 3, or an int greater than 10
    """
    sides = raw_input("How many sides does your shape have? Enter a number between 3 and 10: ")

    if sides == "3":
        print("Triangle")
    elif sides == "4":
        print("Quadrilateral")
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
    elif sides < "3" or sides > "10":
        print("Error")

name_that_shape()