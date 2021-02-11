"""
Program 1
Title: Google
Description:
	Write a function "GoogleLove()" that takes a list and returns a string . 
	Your input should be numbers having 1,2,3,4,5,6,7,8(zero and nine are not be included). 
	Consider the following rules for returning the string
		1, 2, 3, 4 = g, o, l, e
		5 Corresponding to up case of letter before this.
		6 Add a point to the end.
		7 Change case of the first letter.
		8 Reverse the string.
	Consider the example
		GoogleLove(["12213467"])-> "Google."
Author: akashroshan135
Date: 11-Feb-2021
"""

def GoogleLove(numbers):
	string = []
	for i in range(len(numbers)):
		if numbers[i] == '1':
			string.append('g')
		elif numbers[i] == '2':
			string.append('o')
		elif numbers[i] == '3':
			string.append('l')
		elif numbers[i] == '4':
			string.append('e')
		elif numbers[i] == '5':
			string.append(string.pop().upper())
		elif numbers[i] == '6':
			string.append('.')
		elif numbers[i] == '7':
			string[0] = string[0].upper()
		elif numbers[i] == '8':
			string.reverse()
		else:
			print("Invalid character")
	return "".join(string)

nums = input("Enter the numbers (1-8) : ")
print(GoogleLove(list(nums)))