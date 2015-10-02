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
    key_answer = raw_input("""In order for us to guide you, please press 'y' for "yes" and 'n' for "no."
Is the car silent when you turn the key? """)

#battery terminal branches

    if key_answer == "y":
        battery_answer = raw_input("Are the battery terminals corroded? ")
        if battery_answer == "y":
            print("Clean terminals and start again.")
        elif battery_answer == "n":
            print("Replace cables and try again.")
        else:
            print("ERROR: Press 'y' or 'n' in order for us to guide you. Please start again.")

#car click branches

    if key_answer == "n":
        click_answer = raw_input("Does the car make a clicking noise? ")
        if click_answer == "y":
            print("Replace the battery.")
        elif click_answer == "n":
            fail_answer = raw_input("Does the car crank up but fail to start? ")
        else:
            print("ERROR: Press 'y' or 'n' in order for us to guide you. Please start again.")


#fail to start branches

        if fail_answer == "y":
            print("Check spark plug connections.")
        elif fail_answer == "n":
            start_answer = raw_input("Does the engine start then die? ")
        else:
            print("ERROR: Press 'y' or 'n' in order for us to guide you. Please start again.")

#start and die branches
        if start_answer == "y":
            fuel_answer = raw_input("Does your car have fuel injection? ")
        elif start_answer == "n":
            print("Then go ahead and drive.")
        else:
            print("ERROR: Press 'y' or 'n' in order for us to guide you. Please start again.")

#fuel injection branches
        if fuel_answer == "y":
            print("Get it in for service.")
        elif fuel_answer == "n":
            print("Check to ensure the choke is opening and closing.")
        else:
            print("ERROR: Press 'y' or 'n' in order for us to guide you. Please start again.")


#something is wrong. If the program is run, it will work, but there are red notices that pop up too
#despite the program running all the way.
#this will have to be investigated...

diagnose_car()