from functools import wraps
from time import time
def speed_test(fn):
	@wraps(fn)
	def wrapper(*args,**kwargs):
		if wrapper == sum_nums_gen:
			start_time = time()
			print(f"The result is: {fn(*args,**kwargs)}")
			return f"Time elapsed for adding the numbers using a\
 generator expression (function executed: {fn.__name__}): {time() - start_time}"
		else:
			start_time = time()
			print(f"The result is: {fn(*args,**kwargs)}")
			return f"Time elapsed for adding the numbers using a\
 list (function executed: {fn.__name__}): {time() - start_time}"
	return wrapper

@speed_test
def sum_nums_gen(n):
	return sum(i for i in range(1,n+1)) # usimg a generator expression

@speed_test
def sum_nums_list(n):
	return sum([i for i in range(1,n+1)]) # using a list

print(sum_nums_gen(4000000))
print(sum_nums_list(4000000))