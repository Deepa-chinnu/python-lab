"""
Title: Check for anagrams
Description: Given 2 strings, a and b, return true if the strings are anagrams
Author: akashroshan135
Date: 29-Jan-2021
"""

def anagram(a, b):
	if sorted(a) == sorted(b):
		return True
	return False


text1 = input("Enter a string : ")
text2 = input("Enter another string : ")

print(anagram(text1, text2))