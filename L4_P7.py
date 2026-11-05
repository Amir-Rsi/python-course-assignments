# -*- coding: utf-8 -*- 
"""
In the name of God.
Created on Tue Nov  3 21:08:08 2026

@author: amirrsi
L4_P7
"""

numb1 = float(input("please enter the first number: "))
numb2 = float(input("please enter the second number: "))

operation = input ("which operation would you prefer to be done (jam, tafrigh, zarb, taghsim)? ") 
if operation == "jam":
    print(numb1 + numb2)
elif operation == "tafrigh":
    print(numb1 - numb2)
elif operation == "zarb":
    print(numb1 * numb2)
elif operation == "taghsim":
    if numb2 == 0 :
        raise ValueError ("cannot be devided by zero")
    else:
        print(numb1 / numb2)
    
else: 
    print ("choose only from the operations mentioned above!")