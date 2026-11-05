# -*- coding: utf-8  -*-
"""
In the name of God.
Created on Tue Nov  3 00:03:22 2026

@author: amirrsi
L4_P4
"""

product_price = float (input("enter the product price: "))
if product_price > 1000000 :
    print ("free shipping")
elif product_price > 500000 :
    print ("the shipping cost is 30000")
else: print ("the shipping cost is 60000")

