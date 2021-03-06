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

    Inputs: only a raw_input of "Y" or "N"

    Expected Outputs: a progression that builds on the previous question, depending on the answer of "Y" or "N"

    Errors: none.

    Testing:

    Test 1:
    input: Y
    output: "Are the battery terminals corroded?"
    input: Y
    output: "Clean terminals and start again."

    Test 2:
    input: Y
    output: "Are the battery terminals corroded?"
    input: N
    output: "Replace cables and try again."

    Test 3:
    input: N
    output: "Does the car make a clicking noise?"
    input: Y
    output: "Replace the battery."

    Test 4:
    input: N
    output: "Does the car make a clicking noise?"
    input: N
    output: "Does the car crank up but fail to start?
    input: Y
    output: "Check spark plug connections."

    Test 5:
    input: N
    output: "Does the car make a clicking noise?"
    input: N
    output: "Does the car crank up but fail to start?
    input: N
    output: "Does the engine start and then die?"
    input: N
    output: "Engine is not getting enough fuel. Clean fuel pump."

    Test 6:
    input: N
    output: "Does the car make a clicking noise?"
    input: N
    output: "Does the car crank up but fail to start?
    input: N
    output: "Does the engine start and then die?"
    input: Y
    output: "Does your car have fuel injection?"
    input: N
    output: "Check to ensure the choke is opening and closing."

    Test 7:
    input: N
    output: "Does the car make a clicking noise?"
    input: N
    output: "Does the car crank up but fail to start?
    input: N
    output: "Does the engine start and then die?"
    input: Y
    output: "Does your car have fuel injection?"
    input: Y
    output: "Get it in for service."


    """
#Diagonistic steps are represented by 'diag', with the number referring to diagnostic progression

    diag1 = raw_input("Is the car silent when you turn the key?: ")
    if diag1 == "Y":
        diag2 = raw_input("Are the battery terminals corroded?: ")
        if diag2 == "Y":
            print("Clean terminals and try starting again.")
        elif diag2 == "N":
            print("Replace cables and try again.")
    elif diag1 == "N":
        diag3 = raw_input("Does the car make a clicking noise?: ")
        if diag3 == "Y":
            print("Replace the battery.")
        elif diag3 == "N":
            diag4 = raw_input("Does the car crank up but fail to start?: ")
            if diag4 == "Y":
                print("Check spark plug connections.")
            elif diag4 == "N":
                diag5 = raw_input("Does the engine start then die?: ")
                if diag5 == "Y":
                    diag6 = raw_input("Does your car have fuel injection?: ")
                    if diag6 == "N":
                        print("Check to ensure the choke is opening and closing.")
                    elif diag6 == "Y":
                        print("Get it in for service.")
                elif diag5 == "N":
                    print("Engine is not getting enough fuel. Clean fuel pump.")

#diagnose_car()