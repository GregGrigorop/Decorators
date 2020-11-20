from functools import wraps
def ensure_no_kwargs(fn):
	@wraps(fn)
	def wrapper(*args,**kwargs):
		if kwargs: # if kwargs are passed into the greet function this becomes true
			raise ValueError("No kwargs allowed")
		return fn(*args,**kwargs)
	return wrapper

@ensure_no_kwargs
def greet(name):
	print(f"hi there {name}")

greet("Jimmy")
greet(name="Jimmy")