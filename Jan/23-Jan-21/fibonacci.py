"""
Title: Print fibonacci series
Description: Prints fibonacci series till the number specified
Author: akashroshan135
Date: 23-Jan-2021
"""

# function to print fibonacci series
def fib(num):
	a, b = 0, 1
	while a < num:
		print(a, end=" ")
		a, b = b, a + b

num = int(input("Enter a number : "))

fib(num)
