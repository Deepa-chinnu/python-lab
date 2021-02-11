"""
Program 1
Title: Logomaniac
Description:
	Write a function "MyPassion()" which takes in a sentence (a minimum of 5 words) 
	and returns back a dictionary indicating the “mode” of each word. "mode" of a 
	set of data is the data point that appears most frequently , mode of 
	"Taradiddle" is "d". Set of data can, in fact, have multiple modes, so 
	"tomato" has "t", "o" as mode. Note, though, that if all data appears the 
	same number of times there is no mode, like in "dog". Consider the 
	following example :
		MyPassion("tomato are redder")-> {"tomato":["t","o"],"are":[],"redder":[]}
Author: akashroshan135
Date: 11-Feb-2021
"""

def MyPassion(str):
	# splits each word in the sentence to an element in a list
	words = str.split()
	# creates an empty list called collection
	collection = {}
	# checks for each word in the list
	for word in words:
		# obtains the characters that appeared the most
		# creates an empty list
		characters = {}
		max_freq = 0
		# checks each character in the word, set(word) is used to reduce iterations
		for char in set(word):
			# obtains count of the character
			count = word.count(char)
			# if the count is greater, creates a new list and appends it
			if count > max_freq:
				characters = {}
				characters[char] = max_freq = count
				# if the count is the same, appends the character to the list
			if count == max_freq:
				characters[char] = count
		# checks if its an isogram
		if sorted(list(characters)) == sorted(set(word)):
			characters = {}
		# adds the final list to the collection list
		collection[word] = list(characters)
	return collection

str = input("Enter a sentence : ")
print(MyPassion(str.lower()))