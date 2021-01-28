"""
Title: Append string
Description: Append string 2 inbetween string 1
Author: akashroshan135
Date: 28-Jan-2021
"""

#text1 = input("Enter a string : "))
#text2 = input("Enter another string : "))
text1 = "python"
text2 = "aaaaaa"
mid = int(len(text1) / 2)
text = text1[:mid] + text2 + text1[mid:]
print(text)