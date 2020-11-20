from functools import wraps
from time import sleep # the sleep function suspends execution of the current thread for a given
def delay(time): # number of seconds (it pauses code execution for a certain amount of time)
	def inner(fn):
		@wraps(fn)
		def wrapper(*args,**kwargs):
			print(fn.__doc__)
			print(f"Waiting {time}s before running {fn.__name__}")
			sleep(time)
			return fn(*args,**kwargs)
		return wrapper
	return inner

@delay(3)
def say_hi():
	"""this function will greet you"""
	return "hi"

print(say_hi())