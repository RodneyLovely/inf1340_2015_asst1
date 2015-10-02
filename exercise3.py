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


#error message at start
    else:
        print("ERROR: Press 'y' or 'n' in order for us to guide you. Please start again.")

diagnose_car()