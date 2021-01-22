"""
Title: Checks if number is prime
Author: akashroshan135
Date: 22-Jan-2021
"""

num = int(input("Enter a number : "))
# if the number is greater than one
if num > 1:
	# checks if the number is divisble from 2 to num
	for i in range(2, num):
		if (num % i == 0):
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")
# if the number is less than or equal to 1
else:
	print(num, "is a prime number")
