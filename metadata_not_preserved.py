def log_function_data(fn):
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

print(add(10,20))

# a problem when using decorators: if we use __name__ or __doc__ or help() on a decorated (wrapped)
# function outside the wrapper function the documentation etc returned comes from the wrapper
# function and not the decorated function (everything refers to wrapper instead of add)

print(add.__doc__) # prints "I AM THE WRAPPER FUNCTION" instead of "This function adds 2 numbers"
print(add.__name__) # prints "wrapper" instead of "add"
help(add) # prints info from the wrapper and not add