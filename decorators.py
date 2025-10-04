
# Python Decorators - Concepts and Examples
# ========================================

# 1. Basic Decorator
# ------------------
# A decorator is a function that takes another function and extends its behavior without explicitly modifying it.
def basic_decorator(func):
	def wrapper():
		print("Before function call")
		func()
		print("After function call")
	return wrapper

@basic_decorator
def greet():
	print("Hello from the basic decorator!")

greet()

# 2. Multiple Decorator Calls
# ---------------------------
# You can apply multiple decorators to a single function. They are applied from the closest to the function outward.
def decorator_one(func):
	def wrapper():
		print("Decorator One")
		func()
	return wrapper

def decorator_two(func):
	def wrapper():
		print("Decorator Two")
		func()
	return wrapper

@decorator_one
@decorator_two
def multi_greet():
	print("Hello from multiple decorators!")

multi_greet()

# 3. Arguments in the Decorated Function
# --------------------------------------
# Decorators can handle functions with arguments by using *args and **kwargs.
def print_args_decorator(func):
	def wrapper(*args, **kwargs):
		print(f"Arguments were: {args}, {kwargs}")
		return func(*args, **kwargs)
	return wrapper

@print_args_decorator
def add(a, b):
	print(f"Sum: {a + b}")

add(5, 7)

# 4. *args and **kwargs in Decorators
# -----------------------------------
# *args and **kwargs allow decorators to work with any number of positional and keyword arguments.
def universal_decorator(func):
	def wrapper(*args, **kwargs):
		print("Universal decorator called")
		return func(*args, **kwargs)
	return wrapper

@universal_decorator
def show_info(name, age=None):
	print(f"Name: {name}, Age: {age}")

show_info("Sharjeel", age=25)

# 5. Decorator With Arguments
# --------------------------
# You can create decorators that accept their own arguments by adding another function layer.
def repeat(n):
	def decorator(func):
		def wrapper(*args, **kwargs):
			for _ in range(n):
				func(*args, **kwargs)
		return wrapper
	return decorator

@repeat(3)
def say_hi():
	print("Hi!")

say_hi()

# 6. Multiple Decorators
# ----------------------
# Demonstrates stacking multiple decorators and their order of execution.
def uppercase_decorator(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		return result.upper()
	return wrapper

def exclaim_decorator(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		return result + "!"
	return wrapper

@exclaim_decorator
@uppercase_decorator
def get_message():
	return "hello world"

print(get_message())  # Output: HELLO WORLD!

# 7. Preserving Function Metadata
# ------------------------------
# Using functools.wraps to preserve the original function's metadata (like __name__, __doc__)
import functools

def meta_decorator(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		print("Meta-decorator called")
		return func(*args, **kwargs)
	return wrapper

@meta_decorator
def original_function():
	"""This is the original function's docstring."""
	print("Original function executed.")

original_function()
print(original_function.__name__)  # Output: original_function
print(original_function.__doc__)
