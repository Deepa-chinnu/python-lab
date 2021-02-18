"""
Title: Super-sleuth
Description:
	Write a function called decodeMorse() which takes in a string of symbols ".", "-" does two 
	levels of decode first gives it in for "di","dah" , "dit" and then the English alphabet or 
	digits or punctuation mark. Your function should print both the levels of decoding. Validate 
	the input , the function should not take only "." , "-" Note that after each character there
	is a single space and between words two spaces.
Author: akashroshan135
Date: 18-Feb-2021
"""

# dictionary with the character key and its corresponding morse code value
morse = {
	# for alphabets
	'A' : 'di-dah',
	'B' : 'dah-di-di-dit',
	'C' : 'dah-di-dah-dit',
	'D' : 'dah-di-dit',
	'E' : 'dit',
	'F' : 'di-di-dah-dit',
	'G' : 'dah-dah-dit',
	'H' : 'di-di-di-dit',
	'I' : 'di-dit',
	'J' : 'di-dah-dah-dah',
	'K' : 'dah-di-dah',
	'L' : 'di-dah-di-dit',
	'M' : 'dah-dah',
	'N' : 'dah-dit',
	'O' : 'dah-dah-dah',
	'P' : 'di-dah-dah-dit',
	'Q' : 'dah-dah-di-dah',
	'R' : 'di-dah-dit',
	'S' : 'di-di-dit',
	'T' : 'dah',
	'U' : 'di-di-dah',
	'V' : 'di-di-di-dah',
	'W' : 'di-dah-dah',
	'X' : 'dah-di-di-dah',
	'Y' : 'dah-di-dah-dah',
	'Z' : 'dah-dah-di-dit',
	# for digits
	'0' : 'dah-dah-dah-dah-dah',
	'1' : 'di-dah-dah-dah-dah',
	'2' : 'di-di-dah-dah-dah',
	'3' : 'di-di-di-dah-dah',
	'4' : 'di-di-di-di-dah',
	'5' : 'di-di-di-di-dit',
	'6' : 'dah-di-di-di-dit',
	'7' : 'dah-dah-di-di-dit',
	'8' : 'dah-dah-dah-di-dit',
	'9' : 'dah-dah-dah-dah-dit',
	# for special characters
	'&' : 'di-dah-di-di-dit',
	"'" : 'di-dah-dah-dah-dah-dit',
	'@' : 'di-dah-dah-di-dah-dit',
	')' : 'dah-di-dah-dah-di-dah',
	'(' : 'dah-di-dah-dah-dit',
	':' : 'dah-dah-dah-di-di-dit',
	',' : 'dah-dah-di-di-dah-dah',
	'=' : 'dah-di-di-di-dah',
	'!' : 'dah-di-dah-di-dah-dah',
	'.' : 'di-dah-di-dah-di-dah',
	'-' : 'dah-di-di-di-di-dah',
	'×' : 'dah-di-di-dah',
	'+' : 'di-dah-di-dah-dit',
	'"':  'di-dah-di-di-dah-dit',
	'?' : 'di-di-dah-dah-di-dit',
	'/' : 'dah-di-di-dah-dit',
	# '%' : 'dah-dah-dah-dah-dah dah-di-di-dah-dit dah-dah-dah-dah-dah', # * prints 0/0

}

def decodeMorse(str):
	# replaces all '.' to di
	str = list(map(lambda x: 'di' if x == '.' else x, list(str)))
	# replaces all '-' to dah
	str = list(map(lambda x: 'dah' if x == '-' else x, list(str)))

	# replaces the last 'di' to 'dit' in the sentence
	if str[-1:] == ['di']:
		str.pop()
		str.append('dit')

	# splits each word into an item on the list 'words'. Also replaces extra '-' from the join()
	words = '-'.join(str).replace('di- ', 'dit- ').replace('- -', ' ').replace('  -', '  ').split('  ')
	# splits each character in each word into a character list inside the words list
	chracters = [i.split(' ') for i in words]

	# creates a new dictionary by flipping the key and values pairs
	morse_flip = {v: k for k, v in morse.items()}

	# empty list to have the decoded string
	sentence = []

	# new = list(map(lambda y: (list(map(lambda x: morse_flip[x], y)), chracters)))
	# print(new)

	for char in chracters:
		# replaces the morse key to its corresponding character value and appends the character to the list
		sentence.append(''.join(list(map(lambda x: morse_flip[x], char))))

	print(' '.join(words))
	print(' '.join(sentence))


# morseCode = '- .... .. ...  .. ...  ..-. ..- -.' # * prints THIS IS FUN
# morseCode = '.-..-. - .... .. ...  .. ...  ..-. ..- -. .-..-.' # * prints "THIS IS FUN"
morseCode = input("Enter the morse code (use single space to separate characters and double space to separate words) :\n")

# morseCode = ' '.join(morseCode.split())

# filters the list to only have the following characters
allowed_list = ['.', '-', ' ', '  ']
morseCode = ''.join([x for x in morseCode if x in allowed_list])
decodeMorse(morseCode)
