# -*- coding: utf-8 -*- 
"""
Created on Tue Nov  3 00:14:32 2026

@author: amirrsi
L4_P5
"""
#method 1
password = input ("enter your password: ") 
if len(password) < 8 :
    print ("password is short")
    
if password.isdigit() == True:
    print ("password is just made up of numbers")
    
if password.find(" ") != -1:
    print ("can't use space charachter in password")
    
#======================================================== 
#method 2 
password2 = input ("enter your password: ")

if len(password2) < 8 :
    print ("password is short")
elif password2.isdigit() == True:
    print ("password is just made up of numbers") 
elif password2.find(" ") != -1:
    print ("can't use space charachter in password") 
else:
    print("the password format is true!")
#========================================================
#method 3
password3 = input ("enter your password: ")
checks = [len(password3) < 8, password3.isdigit() == True, password3.find(" ") != -1]
if any (checks):
    if len(password3) < 8 :
        print ("password is short")
    elif password3.isdigit() == True:
        print ("password is just made up of numbers") 
    else:
        print ("can't use space charachter in password")
   
else:
    print ("the password format is true!")
     
