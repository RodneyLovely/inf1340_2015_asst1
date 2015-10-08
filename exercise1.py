#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

Expected output:  positive or negative float

Testing:

Test 1:

inputs:
#shares = 100
#purchase_price = 10.00
#broker_commission = 0.05
#sale_price = 15.00

#output = 375.0

"""

#Show the amount of money left after all stock transactions are calculated.

shares = 2000
purchase_price = 900.00
broker_commission = 0.03
sale_price = 942.75

share_purchase = (shares * purchase_price) + (shares * purchase_price * broker_commission)
shares_sale = (shares * sale_price) - (shares * sale_price * broker_commission)
money = shares_sale - share_purchase

print(money)