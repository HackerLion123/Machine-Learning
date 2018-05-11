class Student:
	def __init__(self,name,age):
		self.name,self.age = name,age
	
	def display(self):
		print(self.name,self.age)

	#to apply bool() operation to the classes
	def __bool__(self):
		if self.name != None && self.age != None
			return True

	#to apply len() operation to the classes
	def __len__(self):
		return len(name)+len(age);

Student('bharath',19).display()


""" inheritance in python """

class Person:
	def __init__(self,name):
		self.name = name
	
