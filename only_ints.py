from functools import wraps
def only_ints(fn):
	@wraps(fn)
	def wrapper(*args,**kwargs):
		for i in args: # lines 6-7 both work
			# if any([arg for arg in args if not isinstance(arg,int)]):
			if any([arg for arg in args if type(arg) != int]):
				return "Only invoke with integers"
			return fn(*args,**kwargs)
	return wrapper

@only_ints
def add(x,y):
	return x + y

print(add(1,2))
print(add(1,2.3))
print(add(1,"2"))