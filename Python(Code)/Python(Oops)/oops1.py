#class is basically a blueprint of instances each uniques identity is an instance of class
class Employee:
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay 
		self.email = first + "." + last + "@company.com"

	def fullname(self):
		return '{} {}'.format(self.first, self.last)
	#	return '{} {}'.format(self.first, self.last)

emp_1 = Employee('shubham', 'gupta', '50000') 
emp_2 = Employee('shubi', 'Kumar', '60000')

#print(emp_1)
#print(emp_2)
"""Manual way 
emp_1.first = "Shubham"
emp_1.last = "Gupta"
emp_1.email = "Shubhgupta1209@gmail.com"
emp_1.pay = 50000

emp_2.first = "Shubham"
emp_2.last = "kumar"
emp_2.email = "shuboyoo7@gmail.com"
emp_2.pay = 60000
"""

#print(emp_1.email)
#print(emp_2.email)


emp_1.fullname()
print(Employee.fullname(emp_1))

print(Employee.fullname(emp_2))



#print(emp_2.fullname())
#print('{} {}'.format(emp_1.first, emp_1.last))
#print(emp_1.first)
#print(emp_2.first)
