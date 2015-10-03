#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""


shares = 2000
shares_purchase_price = 900.00
broker_commission = 0.03
shares_sale_price = 942.75

shares_purchase = (shares * shares_purchase_price) + (shares * shares_purchase_price * broker_commission)
shares_sale = (shares * shares_sale_price) - (shares * shares_sale_price * broker_commission)
money = shares_sale - shares_purchase

print(money)