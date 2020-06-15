# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 00:17:55 2019

@author: #sandip
"""

print("Answer some few Question to know your Age! ")
name1 = input("Enter Your First Name: ")
print ("Attention Please!...If you have middle name press Y or else press N....")
flag = input("Press Y/N : ")
flag1 = "y"
flag2 = "n"
name2 = input("Enter Your Middle Name: ")
name3 = input("Enter Your Last Name: ")
#print(name)
year = int(input("Enter your birth Year: "))
#print(year)
present_year = 2019
calc = 2019 - year
#print(calc)
if flag == flag1:
    print("Hello!! Mr.",name1," ",name3,
      '\n',"Your Age is ",calc)
#else:
 #   print("Hello!! Mr.",name1," ",name2," ",name3,
  #    '\n',"Your Age is ",calc)
        
    

print("Thanks! ")
print("Good day!")