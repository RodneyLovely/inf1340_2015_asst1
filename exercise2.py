#!/usr/bin/env python


__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name
    Inputs: int 3, 4, 5, 6, 7, 8, 9, 10
    Expected Outputs: str Triangle, Quadrilateral, Pentagon, Hexagon, Heptagon, Octogon, Nonagon, Decagon
    Errors: any int < 3, or > 10
    """
    number_of_sides = raw_input("How many sides does your shape have? Enter a number between 3 and 10: ")

    if number_of_sides == "3":
        print("Triangle")
    elif number_of_sides == "4":
        print("Quadrilateral")
    elif number_of_sides == "5":
        print("Pentagon")
    elif number_of_sides == "6":
        print("Hexagon")
    elif number_of_sides == "7":
        print("Heptagon")
    elif number_of_sides == "8":
        print("Octogon")
    elif number_of_sides == "9":
        print("Nonagon")
    elif number_of_sides == "10":
        print("Decagon")
    elif number_of_sides < "3" or number_of_sides > "10":
        print("Error")

#name_that_shape()