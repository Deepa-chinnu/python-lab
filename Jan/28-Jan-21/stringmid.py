"""
Title: Print middle characters
Description: Print the middle 2 characters of a string
Author: akashroshan135
Date: 28-Jan-2021
"""

#text = input("Enter a string : "))
text = "python"
mid = int(len(text) / 2)
print(text[mid-1:][:2])