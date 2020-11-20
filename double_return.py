from functools import wraps
def double_return(fn):
	@wraps(fn)
	def wrapper(*args,**kwargs):
		l = []
		l.extend([fn(*args,**kwargs),fn(*args,**kwargs)])
		return l
	return wrapper

@double_return
def add(x,y):
	return x + y

@double_return
def greet(name):
	return f"Hi, I'm {name}"

@double_return
def greet2(name):
	return "Hi, I'm " + name

print(add(1,2))
print(greet('Derrick'))
print(greet2('Jimmy'))