# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 23:31:26 2019

@author: #sandip
"""
print("********************************************")
print("............Age Calculator...................",'\n')
print("Answer some few Question to know your Age! ")
name1 = input("Enter Your First Name: ")
print ("Attention Please!...If you have middle name press Y or else press N....")
flag = input("Press Y/N : ")
#flag1 = "Y"
#flag2 = "N"
if flag == "Y":
   name2 = input("Enter Your Middle Name: ")
   name3 = input("Enter Your Last Name: ")
else:
   name3 = input("Enter Your Last Name: ")
   print(name3)
#print(name)
year = int(input("Enter your birth Year: ",'\n'))
#print(year)
calc = 2019 - year
#print(calc)
print("Results.......",'\n')
if flag == "N":
    print("Hello!! Mr.",name1,name3,
      '\n',"Your Age is ",calc,'\n')
else:
    print("Hello!! Mr.",name1,name2,name3,
    '\n',"Your Age is ",calc,'\n')  
print("!!!How long you have lived your live!!!")   
days = year*365
minutes = year*525948
seconds = year*31553926
print("Mr.",name1,'....\n',"You have been lived exact",days,'days',minutes,'minutes',seconds,'seconds of your life!!')   
print("Thanks! ")