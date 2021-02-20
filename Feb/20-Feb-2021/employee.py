"""
Title: Employee
Description: 
	Write a class called employee which has class variable called company name, company 
	registration number. Instance variables as empname, empid, department, salary. write 
	init method to initialise the instance variables,  method givehike() which hike of 
	10000 if dept is "production" if "development" 8000, "sales" 5000
Author: akashroshan135
Date: 20-Feb-2021
"""

class employee():
	company_name = 'GameStop'
	company_reg = 201

	def __init__(self, id, name, dept, salary):
		self.empid = id
		self.empname = name
		self.department = dept
		self.salary = salary

	def giveHike(self):
		if self.department == 'production':
			self.salary += 10000
		elif self.department == 'development':
			self.salary += 8000
		elif self.department == 'sales':
			self.salary += 5000
		return self.salary

emp1 = employee(1, 'name', 'production', 50000)
print('salary = ', emp1.salary)
emp1.giveHike()
print('salary = ', emp1.salary)
