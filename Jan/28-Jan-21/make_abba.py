"""
Title: Make abba
Description: Given 2 strings, a and b, return a string of the form a+b+b+a
Author: akashroshan135
Date: 28-Jan-2021
"""

def make_abba(a, b):
	return a + b + b + a

text1 = input("Enter a string : ")
text2 = input("Enter another string : ")
print(make_abba(text1, text2))