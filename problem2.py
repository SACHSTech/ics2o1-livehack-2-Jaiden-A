'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:	A program that tells you to input three side lengths and determines whether it is a triangle or not

Author:	Adhvaryu.J

Created:	23/02/2021
------------------------------------------------------------------------------
'''

# get side lengths 
side_1 = float(input("Enter the length of the first side: "))
side_2 = float(input("Enter the length of the second side: "))
side_3 = float(input("Enter the length of the third side: "))

#determine whether it is a triangle or not
if (side_1 + side_2 > side_3) and (side_1 + side_3 > side_2) and (side_2 + side_3 > side_1):
  print("The figure is a triangle")

else:
  print("The figure is NOT a triangle")