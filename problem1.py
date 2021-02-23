'''
-------------------------------------------------------------------------------
Name:		problem1.py
Purpose:	A program that tells the driver if they are fined and the amount owed or if they are clear

Author:	Adhvaryu.J

Created:	23/02/2021
------------------------------------------------------------------------------
'''


# get the speed limit and speed of car
speed_limit = float(input("Enter the speed limit: "))
car_speed = float(input("Enter the recorded speed of the car: "))

# generate the fine values 
no_fine = car_speed < speed_limit
speed_over_limit = car_speed - speed_limit

# compute and show results
if no_fine:
  print("Congratulations, you are within the speed limit")

elif speed_over_limit <= 20:
  print("You are speeding and your fine is $100")

elif (speed_over_limit >= 21) and (speed_over_limit <= 30):
  print("You are speeding and your fine is $270")

else:
  print("You are speeding and your fine is $570")
  