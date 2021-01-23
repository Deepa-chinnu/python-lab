"""
Title: Monkey Trouble
Description: create function monkey_trouble with 2 parameters a_smile, b_smile. 
			 If a_smile and b_smile are true or false, return True. Return False when one is false
Author: akashroshan135
Date: 23-Jan-2021
"""

def monkey_trouble(a_smile, b_smile):
	if ((a_smile and b_smile) or (not a_smile and not b_smile)):
		return True
	return False

print(monkey_trouble(True, True))
print(monkey_trouble(True, False))
print(monkey_trouble(False, True))
print(monkey_trouble(False, False))
