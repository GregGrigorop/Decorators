# Decorators with different arguments (or different signatures)

# def shout(fn):
# 	def wrapper(a):
# 		return fn(a).upper()
# 	return wrapper()

# if we used the above we would encounter an issue when trying to decorate any function that has
# more than 1 argument or no arguments, we'd get a TypeError - that's why we use the following code

def shout(fn):
	def wrapper(*args,**kwargs):
		return fn(*args,**kwargs).upper()
	return wrapper

@shout
def greet(name): # decorated function with 1 argument
	return f"Hi, I am {name}"

@shout
def order(main, side): # decorated function with 2 arguments
	return f"Hi I'd like the {main}, with a side of {side}, thanks"

@shout
def lol(): # decorated function with no arguments
	return "lol"

print(greet('Jimmy'))
print(order('burger','bread'))
print(order(side='burger', main='bread')) # we can also do this
print(lol())
print(greet(name='Derrick'))