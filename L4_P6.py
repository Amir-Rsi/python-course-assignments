# -*- coding: utf-8 -*- 
"""
In the name of God.
Created on Tue Nov  3 20:52:16 2026

@author: amirrsi
L4_P6
"""
class_list = ["Guido Van Rossum", "Ali Pilehvar Meibody", "Amir Rasuli"]
username = input("please enter the username: ")
password = input ("please enter your password: ")
if username.title() not in class_list:
    print ("the user could not be found!")
else:
    if password.lower() == "python123":
        print ("welcome to this class.")
    else:
        print ("password error!")

