"""
Title: Checks if number is a krishnamurthy number
Description: Number whose sum of the factorial of each digit is equal to the number itself
Author: akashroshan135
Date: 22-Jan-2021
"""

# function to obtain the factorial of a num
def factorial(num):
	product = 1
	# loops through all numbers from 1 to num
	# num + 1 ensures num is included in the range
	for i in range(1, num + 1):
		product *= i
	return product


num = int(input("Enter a number : "))

n = num
sum = 0
# loops until all digits are calculated
while n > 0:
	# obtain lsb
	digit = n % 10
	# adds the factorial of the lsb to the sum
	sum += factorial(digit)
	# lsb is discraded
	n //= 10

if sum == num:
	print(num, "is a krishnamurthy number")
else:
	print(num, "is not a krishnamurthy number")

