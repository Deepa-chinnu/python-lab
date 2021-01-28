"""
Title: Combo string
Description: Given 2 strings, a and b, return a string of the form short+long+short. 
			 The strings will not be the same length, but they may be empty (length 0).
Author: akashroshan135
Date: 28-Jan-2021
"""

def combo_string(a, b):
	if len(a) > len(b):
		return b + a + b
	return a + b + a

text1 = input("Enter a string : ")
text2 = input("Enter another string : ")

print(combo_string(text1, text2))