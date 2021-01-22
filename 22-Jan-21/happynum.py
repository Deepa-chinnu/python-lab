"""
Title: Checks if number is "happy"
Description: The squares of the individual digits will ulitimatly lead to 1
Author: akashroshan135
Date: 22-Jan-2021
"""

num = int(input("Enter a number : "))
n = num
sum = 0
# loops if the number has more than 2 digits
while num > 9:
	sum = 0
	# obtains the sum of all the squares of each individual digit
	while num > 0:
		digit = num % 10
		sum += (digit ** 2)
		num //= 10
	num = sum

if sum == 1:
	print(n, "is a happy number")
else:
	print(n, "is not a happy number")