#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

#Calculate the amount spent on the share purchase, including the commission paid to broker
#Calculate the amount made from the share sale, less the commission paid to broker
#Calculate the difference between the share sale and the share purchase
#output should be a positive or negative float

#tested with:
#shares = 100
#purchase_price = 10.00
#broker_commission = 0.05
#sale_price = 15.00
#output = 375.0

shares = 2000
purchase_price = 900.00
broker_commission = 0.03
sale_price = 942.75

share_purchase = (shares * purchase_price) + (shares * purchase_price * broker_commission)
shares_sale = (shares * sale_price) - (shares * sale_price * broker_commission)
money = shares_sale - share_purchase

print(money)