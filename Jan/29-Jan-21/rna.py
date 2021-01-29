"""
Title: DNA to RNA
Description: Given a string, convert all 'T' into a 'U'
Author: akashroshan135
Date: 29-Jan-2021
"""

# using loops
def toRNA_loop(text):
	text = list(text)
	for i in range(len(text)):
		if text[i] == 'T':
				text[i] = 'U'
	return "".join(text)

# using string fn
def toRNA(text):
	text = text.replace('T' , 'U') 

text = input("Enter a string : ")

# print(toRNA(text.upper()))
# print(toRNA_loop(text.upper()))
print(text.upper().replace('T' , 'U'))
