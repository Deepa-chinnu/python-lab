"""
Program 2
Title: Newbie Programs
Description:
	AppleOrangeBanana()- The function returns
		i. string “Apple” if the input is string
		ii. string “Orange” if the input is number
		iii. string “Banana” for anything else

	Gerund()- This function returns
		i. A string prefixed with to if it is ending with “ing”
		ii. A string “Not a gerund” if does not end with “ing”
		Example Gerund(“Painting”)-> to paint

	DNAtoRNA() This functions takes in a DNA string and returns back RNA. Some information for your understanding is given below
		Given a DNA strand, return its RNA complement (per RNA transcription).
		Both DNA and RNA strands are a sequence of nucleotides.
		The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).
		The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).
		Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
			· G -> C
			· C -> G
			· T -> A
			· A -> U
Author: akashroshan135
Date: 04-Feb-2021
"""

def AppleOrangeBanana(str):
	if str.isalpha():
		return "Apple"
	if str.isdigit():
		return "Orange"
	return "Banana"

def Gerund(text):
	if text[-3:] == "ing":
		return "to " + text[:-3]
	return "Not a gerund"

def DNAtoRNA(text):
	text = list(text.upper())
	for i in range(len(text)):
		if text[i] == 'G':
			text[i] = 'C'
		elif text[i] == 'C':
			text[i] = 'G'
		elif text[i] == 'T':
			text[i] = 'A'
		elif text[i] == 'A':
			text[i] = 'U'
		else:
			return "DNA sequence is wrong"
	return "".join(text)

def printMenu():
	print("""----------- MENU -----------
1. AppleOrangeBanana
2. Gerund
3. DNAtoRNA
4. Exit
----------------------------""")

loop = True
while loop:
	text = input("Enter a string : ")
	printMenu()
	choice = int(input("Enter your choice: "))
	if choice == 1:
		print(AppleOrangeBanana(text))
	elif choice == 2:
		print(Gerund(text))
	elif choice == 3:
		print(DNAtoRNA(text))
	else:
		print("Program will exit")
		loop = False