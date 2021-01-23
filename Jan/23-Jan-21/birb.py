"""
Title: Parrot Trouble
Description: True when talking and the hour is before 7 or after 20. Return false otherwise.
Author: akashroshan135
Date: 23-Jan-2021
"""

def parrot_trouble(talking, hour):
	if talking and (hour < 7 or hour > 20):
		return True	
	return False

print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))
