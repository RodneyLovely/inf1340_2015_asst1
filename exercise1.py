#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""


__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Calculate amount spent on stock
# Calculate commission paid to broker for purchase
# Calculate amount made on sale of stock
# Calculate commission paid to broker for sale
# Calculate difference between money made and spent

number_of_shares = 2000
unit_price_purchase = 900.00
commission_on_sale = .03
purchase_price = number_of_shares * unit_price_purchase
amount_paid_to_broker_for_purchase = purchase_price * commission_on_sale

print(number_of_shares * unit_price_purchase)
print(purchase_price * commission_on_sale)
print(purchase_price + amount_paid_to_broker_for_purchase)

unit_price_sale = 942.75
sale_price = (unit_price_sale * number_of_shares)
commission_paid_to_broker_for_sale = sale_price * commission_on_sale
money_made_on_sale = sale_price - commission_paid_to_broker_for_sale

print(sale_price)
print(commission_paid_to_broker_for_sale)
print(money_made_on_sale)

net_profit = money_made_on_sale - (purchase_price + amount_paid_to_broker_for_purchase)
print(net_profit)

money = net_profit
print(money)


# this is just a rough of the code
# we would only need to have the final print function for what we hand in
# I removed all of the extra print functions in pythontutor.com and it works
#also checks out on paper