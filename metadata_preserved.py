from functools import wraps
def log_function_data(fn):
	@wraps(fn)
	def wrapper(*args,**kwargs):
		"""I AM THE WRAPPER FUNCTION"""
		print(f"You are about to call the wrapped function {fn.__name__}")
		print(f"Here's the documentation: {fn.__doc__}")
		return fn(*args,**kwargs)
	return wrapper

@log_function_data
def add(x,y):
	"""This function adds 2 numbers"""
	return x + y

print(add(20,30))
print(add.__doc__)
print(add.__name__)
help(add)