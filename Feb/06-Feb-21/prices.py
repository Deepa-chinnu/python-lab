"""
Title: Prices
Description: Exercise 2 in 
	https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/content/lists/exercises_list_and_dictionaries.html
Author: akashroshan135
Date: 06-Feb-2021
"""

prices = {
	"banana": 4,
	"apple": 2,
	"orange": 1.5,
	"pear": 3
}
stock = {
	"banana": 6,
	"apple": 0,
	"orange": 32,
	"pear": 15
}
total = 0
for key in prices:
	print(key, "\nprice :", prices[key], "\nstock :", stock[key], "\n")
	total += prices[key] * stock[key]
print("Total = ", total)