#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""


__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


shares = 2000
share_cost = 900.00
broker_commission = (shares * share_cost) * 0.03

#Two weeks later...

share_sale = 942.75
broker_commission = (shares * share_sale) * 0.03 + broker_commission
Lakshmi_total = (shares * share_sale - shares * share_cost) - broker_commission

if (Lakshmi_total < 0):
    print("Lakshmi lost money, at a total of: " + str(Lakshmi_total) + " dollars.")
else:
    print("Lakshmi made a profit, at a total of: " + str(Lakshmi_total) + " dollars.")
