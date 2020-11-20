# creating a decorator that accepts an argument
from functools import wraps
def ensure_first_arg_is(val):
	def inner(fn):
		@wraps(fn)
		def wrapper(*args,**kwargs):
			if not args:
				return "There are no args"
			if args[0] != val:
				return f"The first arg needs to be {val}"
			return fn(*args,**kwargs)
		return wrapper
	return inner

@ensure_first_arg_is("ice cream")
def fav_foods(*foods):
	return foods

@ensure_first_arg_is(10)
def add_to_ten(num1,num2):
	return num1 + num2

print(fav_foods('burrito','ice cream'))
print(fav_foods('ice cream', 'burrito'))
print(fav_foods())

print(add_to_ten(10,20))
print(add_to_ten(1,10))
print(add_to_ten())