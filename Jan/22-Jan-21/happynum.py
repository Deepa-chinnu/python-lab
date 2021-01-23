"""
Title: Checks if number is "happy"
Description: The sum of the squares of the individual digits will ulitimatly lead to 1
Author: akashroshan135
Date: 22-Jan-2021
"""

num = int(input("Enter a number : "))
n = num
sum = 0
# loops until the number is 1 or 4. 4 results in an infinite loop
while(n != 1 and n != 4):
#while n != 1:
	sum = 0
	# obtains the sum of all the squares of each individual digit
	while n > 0:
		# obtain lsb
		digit = n % 10
		# adds the square of the lsb to the sum
		sum += (digit ** 2)
		# lsb is discraded
		n //= 10
	#print(sum)
	# assigned to repeat with the new sum
	n = sum

if sum == 1:
	print(num, "is a happy number")
else:
	print(num, "is not a happy number")