"""
Title: Checks if year is a leap year
Author: akashroshan135
Date: 22-Jan-2021
"""

# int is used to typecast the string input into an integer
# input is used to accept string input data
year = int(input("Enter year to be checked : "))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
	print(year, "is a leap year")
else:
	print(year, "is not a leap year")