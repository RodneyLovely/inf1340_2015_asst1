#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:

    Expected Outputs:

    Errors:

    """

    error = ("ERROR: Remember to enter 'y' or 'n' in order for us to guide you. "
            "Please restart the program.")

    key = raw_input("""In order for us to guide you, please press 'y' for "yes" and 'n' for "no."
Is the car silent when you turn the key? """)

    if key == "y":
        battery = raw_input("Are the battery terminals corroded? ")
        if battery == "y":
            print("Clean terminals and try starting again.")
        elif battery == "n":
            print("Replace cables and try again.")
        else:
            print(error)

    elif key == "n":
        click = raw_input("Does the car make a clicking noise? ")
        if click == "y":
            print("Replace the battery.")
        elif click == "n":
            crank = raw_input("Does the car crank up but fail to start? ")
            if crank == "y":
                print("Check spark plug connections.")
            elif crank == "n":
                engine = raw_input("Does the engine start and then die? ")
                if engine == "n":
                    #I changed the 'print' statement due to the class email from Oct. 7
                    print("Engine is not getting enough fuel. Clean fuel pump.")
                elif engine == "y":
                    fuel = raw_input("Does your car have fuel injection? ")
                    if fuel == "n":
                        print("Check to ensure the choke is opening and closing.")
                    elif fuel == "y":
                        print("Get it in for service.")
                    else:
                        print(error)
                else:
                    print(error)
            else:
                print(error)
        else:
            print(error)
    else:
        print(error)

#I'm not sure if I did it in elegant fashion, but this works at every step
#including an error message if anything but 'y' or 'n' is pressed at any stage
#I think the program could probably be clarified by good identifiers and better readability perhaps


diagnose_car()