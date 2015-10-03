#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

#Calculate the amount Lakshmi spent on the share purchase, including the commission paid to her broker
#Calculate the amount Lakshmi received on the share purchase, including the commission paid to her broker
#Calculate the difference between the amount made on the sale with the amount spent on the purchase
#output should be a positive or negative number

shares = 2000
purchase_price = 900.00
broker_commission = 0.03
sale_price = 942.75

share_purchase = (shares * purchase_price) + (shares * purchase_price * broker_commission)
shares_sale = (shares * sale_price) - (shares * sale_price * broker_commission)
money = shares_sale - share_purchase

print(money)

#tested with:
#shares = 100, 3000, 2000
#purchase_price = 10.00, 175.00, 825.00
#broker_commission = 0.05, 0.03, 0.03
#sale_price = 15.00, 187.50, 862.90
#output = 375.0, 4875.0, -25474.0