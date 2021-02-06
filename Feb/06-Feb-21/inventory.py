"""
Title: Inventory
Description: Exercise 1 in 
	https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/content/lists/exercises_list_and_dictionaries.html
Author: akashroshan135
Date: 06-Feb-2021
"""

inventory = {
	'gold' : 500,
	'pouch' : ['flint', 'twine', 'gemstone'],
	'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50

print(inventory)