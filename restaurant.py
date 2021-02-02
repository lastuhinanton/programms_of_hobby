class Lunch:
	def __init__(self, name):
		self.name = name

	def order(self):
		print(f"Hello, i'm {employee.name}\n")
		return input(f'What do you want, {self.name}?\t')

	def result(self):
		print(f"\nThat's you bill, {self.name}")

class Customer(Lunch):
	def __init__(self, name):
		Lunch.__init__(self, name)
		
	def placeOrder(self):
		import time

		Food.__init__(self, self.order())
		self.printFood()
		time.sleep(5)

		Employee.takeOrder(self, self.food)
		time.sleep(10)
		self.question()
		time.sleep(5)

		print(f'\nThank you, {employee.name}\n'
			'That is for you on tea!')

	def question(self):
		import time
		print('\n\nWaiter, bill, please\n')
		time.sleep(5)
		Lunch.result(self)

	def printFood(self):
		print(f'\nYour order {self.food} will be ready in 15 minutes!\n')

class Employee(Lunch):

	def takeOrder(self, foodName):
		print(f"That's your order, {self.name}\n"
			f"Your {foodName}")

class Food:
	def __init__(self, name):
		self.food = name


employee = Employee('Jane Smith')
customer = Customer('Anton Lastuhin')
customer.placeOrder()