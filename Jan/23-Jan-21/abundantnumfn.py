"""
Title: Checks if number is "abundant" using a function
Description: The sum of the divisors of a given number will be greater than the number itself
Author: akashroshan135
Date: 23-Jan-2021
"""

def abundant(num):
	sum = 0
	# loops for all the numbers from 1 to num 
	for i in range(1, num):
		# checks if num is divisible by i
		if num % i == 0:
			# if divisible, it is added to the sum
			sum += i
	return sum

num = int(input("Enter a number : "))

sum = abundant(num)

# checks if the obtained sum is greater than the num
if sum > num:
	print(num, "is abundant as the sum is", sum)
else:
	print(num, "is not abundant as the sum is", sum)