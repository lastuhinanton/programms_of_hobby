
def loadclass():
	import sys, importlib
	modulename = sys.argv[1]
	# print(modulename)   							#for checking
	module = importlib.import_module(modulename)
	# import validate_properties as module1
	# print(module)									#it hasn't diferent
	# print(module1.CardHolder)						#return same objects of class
	# print(module.CardHolder)
	print('[Using: %s]' % module.CardHolder)
	return module.CardHolder

def printholder(who):
	print(who.acct, who.name, who.age, who.remain, who.addr, sep=' / ')

if __name__ == '__main__':
	CardHolder = loadclass()
	bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
	printholder(bob)
	bob.name = 'Bob Q. Smith'
	bob.age = 50
	bob.acct = '23-45-67-89'
	printholder(bob)
	sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
	printholder(sue)
	anton = CardHolder('1830-83-83', 'Anton Lastuhin', 19, 'USA LA')
	printholder(anton)
	try:
		sue.age = 200
	except:
		print('Bad age for Sue')

	try:
		sue.remain = 5
	except:
		print("Can't set sue.remain")

	try:
		sue.acct = '1234567'
	except:
		print('Bad acct for Sue')

