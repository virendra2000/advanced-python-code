# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 12:29:13 2020

@author: Virendra
"""

import os
print("-------------------------CONTACT BOOK------------------------")
print("1. Add the Contact Number")
print("2. Search the Contact")
print("3. Exit")
d1={}
while True:
    n=int(input("Enter your Option in Integer Form[1/2/3] :-"))
    os.system('cls')
    if n==1:
        name=input("Enter Name\n");1
        phno=input("\nEnter Contact Number\n")
        d1[name]=phno
    elif n==2:
        name1=input("Search Contact Name with Detail")
        print("Contact Number of",name1,"is ",d1[name1])
    else:
        break