from functools import wraps
def ensure_authorized(fn):
	@wraps(fn)
	def wrapper(*args,**kwargs):
		for k in kwargs: # instead of lines 5-6 we could use this: if kwargs.get("role") == "admin":
			if k == 'role' and kwargs[k] == 'admin':
				return fn(*args,**kwargs)
		return "Unauthorized"
	return wrapper

@ensure_authorized
def show_secrets(*args,**kwargs):
	return "Don't tell anybody!"

print(show_secrets(a='Jimmy',role='admin'))
print(show_secrets(role='champion'))
print(show_secrets(a='Derrick'))
print(show_secrets())