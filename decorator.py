def be_polite(fn):
	def wrapper():
		print('What a pleasure to meet you')
		fn()
		print('Have a great day!')
	return wrapper() # a) OR return wrapper

@be_polite
def greet():
	print('My name is Ilias')

@be_polite
def rage():
	print('Relax')

greet # OR greet()
rage # OR rage()
# by using the @be_polite we don't have to use be_polite(greet) & be_polite(rage)