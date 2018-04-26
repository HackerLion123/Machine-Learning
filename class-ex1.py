class Student:
	def __init__(self,name,age):
		self.name,self.age = name,age
	
	def display(self):
		print(self.name,self.age)

Student('bharath',19).display()


""" inheritance in python """

class Person(Student):
	def __init__(self):
	
