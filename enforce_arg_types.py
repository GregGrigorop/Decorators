def enforce(*types):
	def decorator(f):
		def new_func(*args,**kwargs):
			# we convert the tuple args into something mutable
			newargs = []
			for a,t in zip(args,types): # OR: for (a,t) in zip(args,types)
				newargs.append(t(a))
			return f (*newargs,**kwargs)
		return new_func
	return decorator

@enforce(str, int)
def repeat_msg(msg, times):
	for i in range(times):
		print(msg)

@enforce(float, float) # if we're supposed to pass in an int and we pass in a float we'll lose
def divide(a,b): # some data as the float is chopped off, so we select float instead of int here
	print(a/b)

repeat_msg('hi','4')
divide('1','0.5')