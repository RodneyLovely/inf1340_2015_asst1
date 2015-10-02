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
first_answer = raw_input("""In order for us to help you, please enter 'y' for "yes", and 'n' for "no".
Is the car silent when you turn the key? """)

#battery terminals branches

if first_answer == "y":
    key_answer = raw_input("Are the battery terminals corroded? ")
    if key_answer == "y":
        print("Clean terminals and try starting again.")
    else:
        print("Replace cables and try again.")



diagnose_car()